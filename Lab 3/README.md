# Chatterboxes
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Additional Parts

As mentioned during the class, we ordered additional mini microphone for Lab 3. Also, a new part that has finally arrived is encoder! Please remember to pick them up from the TA.

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using a USB microphone, and the speaker on your webcamera. (Originally we intended to use the microphone on the web camera, but it does not seem to work on Linux.) In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

This file can be found in name.py in the uploaded files.

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

One thing you might need to pay attention to is the audio input setting of Pi. Since you are plugging the USB cable of your webcam to your Pi at the same time to act as speaker, the default input might be set to the webcam microphone, which will not be working for recording.

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

Bonus Activity:

If you are really excited about Speech to Text, you can try out [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and [voice2json](http://voice2json.org/install.html)
There is an included [dspeech](./dspeech) demo  on the Pi. If you're interested in trying it out, we suggest you create a seperarate virutal environment for it . Create a new Python virtual environment by typing the following commands.

```
pi@ixe00:~ $ virtualenv dspeechexercise
pi@ixe00:~ $ source dspeechexercise/bin/activate
(dspeechexercise) pi@ixe00:~ $ 
```

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

![image](https://user-images.githubusercontent.com/67603876/135937543-390e9f27-bba1-4b17-8345-692cf8e525fa.png)

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*

Here is the planned dialogue for my device CareBot:

![image](https://user-images.githubusercontent.com/67603876/135937569-f00dd87b-9480-45b1-bbe3-da5ec6b766b8.png)

I first started with the storyboard dialogue and thought about where the user might have answers that do not fit what happened exactly in the storyboard. In those places, I put two branches so that both options would be covered. I did a good job at first making sure the dialogue was explicit enough that there are a limited number of reasonable responses, so this was not difficult.

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

Here is the recording of the dialogue between me and my partner (in a YouTube video because I could not attach an audio file to this page):

[![Watch the video](https://img.youtube.com/vi/won93bKitH8/0.jpg)](https://www.youtube.com/watch?v=won93bKitH8)

In my plans for the dialogue, I made sure to make everything very explicit so that the user does not have to think too much about what to say to get the device to work. In the actual dialogue, though, while this did make some parts very clear according to my partner, it also put some unnecessary pressure on the user. To make things clear, I typically (as seen in the image of the dialogue above) have the device say what it intends to do and tells the user to say something to stop it if they want. This makes it unclear how long the device will wait to hear a signal from the user, and it puts some pressure on the user to say (or not say) the right thing. To fix this, either a clear indication of the time or always giving the user options would be better than just saying the device's intention and asking for acceptance or denial.


### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...

   The main piece of feedback I got was similar to my thoughts from the end of part 1 of the lab. It was that some of the options the device gives put pressure on the user to answer within a certain time frame exactly as they are supposed to. I do not want this device to put pressure on anyone, and I want the user to have the ability to give accurate answers every time. I was told I could use the display to my advantage or maybe even some indication of a timer that tells the reader how long the device is recording for when the user is prompted for a reply.

2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?

   I decided to just focus on vocal inputs because the intended use case of my device is in the situation where the user has their hands tied or is busy doing something. This would make it very difficult for them to use their hands or give any other type of active input to the system. Their voice is the only thing that is free in that scenario. 

3. Make a new storyboard, diagram and/or script based on these reflections.

![Dialogue2](https://user-images.githubusercontent.com/67603876/137246474-e0554014-47f2-43d7-8f95-fae213b89523.PNG)


## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

The system works by running a sequence of interactions that involve the Raspberry Pi speaking to give the user options or a question to answer, and the user replying. Each of these interactions use techniques from part 1 of this lab, like playing sound from the speaker and taking vocal input from the user. I used these techniques to create an interaction helper function, which makes the Raspberry Pi say something, records a reply, and then repeats what the user said in the reply before moving onto the next stage of the process. The Raspberry Pi also displays different things at certain steps in order to make it easier for the user to understand what is happening and react in time.

The "process" is written sequentially in the helper function "run()" and acts as the main actuator of the system. It calls on the helper functions to create vocal interactions, draw things on screen, and make the Raspberry Pi speak. Before this process is started, the current time is displayed so that the user can see when the voice initiates conversation by pointing out how late it is. Then as the interactions progress, the display changes to reflect the current step.

*Include videos or screencaptures of both the system and the controller.*

[![Watch the video](https://img.youtube.com/vi/zf0zVFSIvzg/0.jpg)](https://www.youtube.com/watch?v=zf0zVFSIvzg)


## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
Most of the time, the Raspberry Pi was specific enough to give the user a good idea of what to say, so that worked well.

Sometimes, the microphone would not pick up the words well, especially when I tried it on someone I know with a different accent. Also, at certain points, the user (when the intent was that they should stay silent) did not know what to do and looked confused when the correct option was to stay silent.

### What worked well about the controller and what didn't?

My system is relatively autonomous. When the users followed the exact options I detailed, it worked perfectly, but when they said anything else or wanted to say anything else, the system had no built in response to it, so it defaulted to a different options, which is not good.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

It takes a lot to create a totally autonomous system because of all the different things a user can say. Some NLP might be required to make it work better because that could help consolidate words (like turning "good" and "great" into both "good", etc.) and decipher a user's intent.


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

One thing this device could be used for, if widespread enough, is to gather typical reactions/replies from users across devices to help train the device. If the devices follow the typical trends, it would increase its accuracy in doing what the user intends. Some other sensing modalities that could be useful with a system like this are video so that it could use Emotion Recognition; if the user is angry, maybe the device should cut what it is saying short, etc. 

