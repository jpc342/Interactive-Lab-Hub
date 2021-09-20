import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# ADDED-IN
import random

# new font
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

import datetime as dt

now = dt.datetime.now()
end = dt.datetime.fromisoformat('2029-07-22 21:45:00')
dif = end-now

# Calculate each category of time left
years = dif.days//365
days = dif.days%365
minutes = dif.seconds//60
seconds = dif.seconds%60
hours = minutes//60
minutes = minutes%60

# Environmental tips
tips = ['Use reusable water bottles!','Eat more local food!','Less red meat!','Reusable shopping bags!','Bike more!','Look up local recycling guide!','Conserve water!']
tip = ''  # Initialize to empty string to not display anything before a button is pressed

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py
    
    # Choose random tip to display
    if not buttonA.value or not buttonB.value:
        tip = tips[random.randint(0, len(tips)-1)]

    t = str(years) + 'years ' + str(days) + 'days  ' + str(hours)+':'+str(minutes)+':'+str(seconds)
    x,y = (0,0)
    draw.text((x,y), t, font=font)
    y += font.getsize(t)[1]
    draw.text((x,y), 'Until the end', font=font)
    y += (font.getsize(t)[1])
    draw.text((x,y), 'What can you do to help?', font=font2)
    y += font.getsize(t)[1]
    draw.text((x,y), 'Hold a button (1s) to find out', font=font2)
    y += font.getsize(t)[1]
    draw.text((x,y), tip, font=font2, fill="#00FF00")
    if len(tip)>0: # If user has held the button once already
        y += font.getsize(t)[1]
        draw.text((x,y), 'Hold button again for more', font=font2)
    
    # Update next time
    delta = dt.timedelta(seconds=1)
    dif = dif - delta
    years = dif.days//365
    days = dif.days%365
    minutes = dif.seconds//60
    seconds = dif.seconds%60
    hours = minutes//60
    minutes = minutes%60
    
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
