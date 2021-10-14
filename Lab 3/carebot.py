import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import os
import sys
from vosk import Model, KaldiRecognizer
import wave
import json

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# INITIALIZE SENSOR


# HELPER FUNCTIONS
def pi_speak(s):
    """
    Helper function to make the RPi speaker say something using subprocess and Google text-to-speech
    """
    subprocess.run(['sh', 'Google_speech.sh', s])

def record(list=None):
    """
    Helper function to make the RPi record user voice input, based off the given files in speech2text
    List is the list of acceptable words, default to none
    Returns a string of the user's voice input
    """
    os.system('arecord -D hw:2,0 -f cd -c1 -r 48000 -d 4 -t wav recorded_input.wav')
    f = wave.open('recorded_input.wav', 'rb')
    model = Model('model')
    if list is None:
        rec = KaldiRecognizer(model, f.getframerate())
    else:
        rec = KaldiRecognizer(model, f.getframerate(), list)
    while True:
        data = f.readframes(4000)
        if len(data) == 0:
            break
        rec.AcceptWaveform(data)
    i = json.loads(rec.FinalResult())['text']
    print('You said: ', i)
    return i

def q_a(s, list=None):
    """
    Helper function that makes RPi speak string s, record a reply, then repeat that reply back and return it
    """
    pi_speak(s)
    rep = record(list)
    if rep=='[unk]':
        rep = 'Nothing'
    pi_speak('You said ' + rep)
    return rep

def new_screen(text, font=font):
    """
    Helper function to draw new things on screen
    """
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    x,y = (60,50)
    draw.text((x,y), text, font=font) 
    disp.image(image,rotation)
    
def run():
    """
    Helper function to run the speech recognition in the interaction
    """
    rep = q_a('I will check for the fastest available options. If you want it by price or food type, say one of those instead.', 'price type cuisine [unk]')
    if 'price' in rep or 'type' in rep or 'cuisine' in rep:
        options = ['Burrito Place', 'Astoria Taco Factory']
        pi_speak('Ok, searching by that instead')
    else:
        options = ['Bar and Grill','Sushi and Ramen']
    
    new_screen(options[0] + '\n' + options[1], font2)
    rep = q_a('The best available options are '+options[0]+' and '+options[1]+'. Which would you prefer?', 'bar grill sushi ramen japanese burrito place story taco factory [unk]')
    if 'bar'in rep or 'grill' in rep:
        choice = 'Bar and Grill'
    elif 'sushi' in rep or 'ramen' in rep or 'japanese' in rep:
        choice = 'Sushi and Ramen'
    elif 'burrito' in rep or 'place' in rep:
        choice = 'Burrito Place'
    elif 'story' in rep or 'taco' in rep or 'factory' in rep:
        choice = 'Astoria Taco Factory'
    else:
        choice = 'Restaurant'
    
    new_screen('Say popular for the most popular order', font2)
    rep = q_a('Okay, ordering the last thing you got from '+choice+'. I can also get you their most popular order. Say popular if you want that instead.', 'popular instead [unk]')
    if 'popular' or 'instead' in rep:
        order = choice+'s most popular order'
    else:
        order = 'your last order'
    
    new_screen('Say cancel to cancel the order', font2)
    rep = q_a("Finalizing the order. If you want to cancel, say cancel", 'cancel stop [unk]')
    if "cancel" in rep or "stop" in rep:
        pi_speak("Canceling order. Remember to eat soon!")
    else:
        rep = q_a("Order placed. Enjoy!", 'thank you thanks [unk]')
        if "thank" in rep or "you" in rep or "thanks" in rep:
            pi_speak("No problem, Jay!")

# WHILE LOOP
state = False # state variable to track the state, initialized or not
loop = 0 # while loop iteration counter
while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Display time
    t = time.strftime("%H:%M")
    x,y = (60,50)
    draw.text((x,y), t, font=font) 
    disp.image(image,rotation)

    rep = q_a('Hey, Jay. Its getting late and you have not eaten dinner yet! Lets order something. If you would like to, say yes')
    if "yes" in rep or "yeah" in rep or "sure" in rep or "options" in rep or "ok" in rep:
        run()
    
    loop += 1

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
