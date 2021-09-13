

# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.

For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. 

_Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

### To start the semester, you will need:
1. Set up your own Github "Lab Hub" repository to keep all you work in record by [following these instructions](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md).
2. Set up the README.md for your Hub repository (for instance, so that it has your name and points to your own Lab 1) and [learn how to](https://guides.github.com/features/mastering-markdown/) organize and post links to your submissions on your README.md so we can find them easily.
3. (extra: Learn about what exactly Git is from [here](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F).)

### For this lab, you will need:
1. Paper
2. Markers/ Pens
3. Scissors
4. Smart Phone -- The main required feature is that the phone needs to have a browser and display a webpage.
5. Computer -- We will use your computer to host a webpage which also features controls.
6. Found objects and materials -- You will have to costume your phone so that it looks like some other devices. These materials can include doll clothes, a paper lantern, a bottle, human clothes, a pillow case, etc. Be creative!

### Deliverables for this lab are: 
1. Storyboard
1. Sketches/photos of costumed device
1. Any reflections you have on the process
1. Video sketch of the prototyped interaction
1. Submit the items above in the lab1 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same from each person in the group.

### The Report
This README.md page in your own repository should be edited to include the work you have done (the deliverables mentioned above). Following the format below, you can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in your README.md for the lab.

## Lab Overview
For this assignment, you are going to:

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. Plan 

To stage the interaction with your interactive device, think about:

_Setting:_ Where is this interaction happening? (e.g., a jungle, the kitchen) When is it happening?

_Players:_ Who is involved in the interaction? Who else is there? If you reflect on the design of current day interactive devices like the Amazon Alexa, it’s clear they didn’t take into account people who had roommates, or the presence of children. Think through all the people who are in the setting.

_Activity:_ What is happening between the actors?

_Goals:_ What are the goals of each player? (e.g., jumping to a tree, opening the fridge). 

The interactive device can be anything *except* a computer, a tablet computer or a smart phone, but the main way it interacts needs to be using light.

\*\***Describe your setting, players, activity and goals here.**\*\*

My staged interaction will be a sensor that activates an alarm when a refrigerator is left open. Two sensors are involved: one to check if the fridge is closed, and another to check if a person is standing in front of the fridge.

_Setting_: a kitchen at any time of day

_Players_: the person living there, their refrigerator, alarm system

_Activity_: the player does not close the fridge all the way, and the alarm system lets him know to go back and close it

_Goals_: to prevent wasting energy and food going bad from the fridge losing its cold air

Sketch a storyboard of the interactions you are planning. It does not need to be perfect, but must get across the behavior of the interactive device and the other characters in the scene. 

\*\***Include a picture of your storyboard here**\*\*
![Storyboard](https://user-images.githubusercontent.com/67603876/132416188-615991bb-aa3b-49b4-9166-6ce7963b5f8e.jpg)

Present your idea to the other people in your breakout room. You can just get feedback from one another or you can work together on the other parts of the lab.

\*\***Summarize feedback you got here.**\*\*

The feedback that I received from people I asked about it was that this would be a useful device, and that it would be a good one to try to prototype.

## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

\*\***Are there things that seemed better on paper than acted out?**\*\*

On paper, it seemed much easier to intentionally leave a fridge partially open, but my fridge likes to close by itself and even push things out of the way to do so. To fix this, I placed enough items in the back of the fridge, so that when I put a pot in front of them, the fridge door stayed open. 

It also seemed easier at first to find the right angles to film this, but it took a few different tries to find the right spot.


## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 

If you run into technical issues with this tool, you can also use a light switch, dimmer, etc. that you can can manually or remotely control.

\*\***Give us feedback on Tinkerbelle.**\*\*

I had problems getting Tinkerbelle to work on my devices; although I was able to download and run it on my computer, even when my phone was connected to the same WiFi network, the access page (using the computer's IPv4 address) would not come up on my phone's browser, nor would it show up when I tried using the "local" address on my own computer. This could be because I need to either reinstall or change the location of some Python files because when I cloned and downloaded the Tinkerbelle files, after installing most of the files, a red line appeared:

![image](https://user-images.githubusercontent.com/67603876/132417074-afb8e795-1c82-4b47-b532-5d2b9d61f667.png)

It was unclear what this meant, since it was only trying to uninstall something that was already installed, and since the program still ran even though it did not fully work. I decided not to use it after all because a remote control light is not necessary to show the interaction that my device facilitates. 

## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

\*\***Include your first attempts at recording the set-up video here.**\*\*

Some of my first attempts at filming the video are linked below (click on the image to be taken to the YouTube video). These three clips show me learning that my initial plans for all three of those scenes would not work perfectly. In the first scene, the fridge (as mentioned earlier) does not stay open. In the second, the wrong alarm plays, and the timing with the lights is not even close to synchronized. Finally, in the third clip, I try to hide the phone alarm I use above the fridge so that I can turn it off as I shut the fridge, but not being able to (at the same time) hit the light switch was a problem (so I split this into two clips in the final version).

[![Watch the video](https://img.youtube.com/vi/FQiNGfLGO_M/0.jpg)](https://www.youtube.com/watch?v=FQiNGfLGO_M)

Now, hange the goal within the same setting, and update the interaction with the paper prototype. 

\*\***Show the follow-up work here.**\*\*

Nothing changed in this step with the prototype itself; the only things that changed were the mistakes mentioned above in the video planning/filming.

## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

\*\***Include sketches of what your device might look like here.**\*\*

There were three main ideas of what this device should look like, all shown in this picture:

![image](https://user-images.githubusercontent.com/67603876/132417996-ac61927a-5986-483f-b72a-b7386cc70911.png)

I ended up deciding by the process described below.

\*\***What concerns or opportunitities are influencing the way you've designed the device to look?**\*\*

I want the device (the sensor above the fridge) to look like a motion/distance sensor, which are usually pointed in one direction as opposed to cameras that have a large field of view. It turns out my Glade Plug-In air freshener when rotated looks exactly the way I wanted, and its prongs fit perfectly into the groove above the freezer; this made it the perfect look-alike to the device I was going for. 

I also considered whether or not to have the alarm sound emanate from the sensor itself, but I decided it would be better to imply its integration into a house speaker system or any other speaker in the house, as these are becoming more popular, and a speaker would make the sensor bulkier (and possibly uglier). 

Here is what it looked like in the end (using a black mask and some tape to cover up the Glade controls:



## Part F. Record

\*\***Take a video of your prototyped interaction.**\*\*

[![Watch the video](https://img.youtube.com/vi/zR2wcBsqp98/0.jpg)](https://www.youtube.com/watch?v=zR2wcBsqp98)


\*\***Please indicate anyone you collaborated with on this Lab.**\*\*
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

The main inspiration behind my idea was from the example shown in class by Panda Xu from last spring (the microwave device). The secondary was when I was talking to my Mom on the phone, and she mentioned that she had forgotten to close the fridge the day before.


# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.


## Prep (to be done before Lab on Wednesday)

You will be assigned three partners from another group. Go to their github pages, view their videos, and provide them with reactions, suggestions & feedback: explain to them what you saw happening in their video. Guess the scene and the goals of the character. Ask them about anything that wasn’t clear. 

\*\***Summarize feedback from your partners here.**\*\*

I turned my first lab in late, so I was not partnered up with anyone for feedback. However, I asked some people in the class for feedback on my own (and gave them "unofficial" feedback, as well). One piece of feedback I got was that it did not make much sense that the overhead lights should not be what actuates the notification that the fridge is still open because it is too big/annoying, especially considering the user might do that on purpose for some reason; there also is no clear way to turn the alarm off if this is the case. This is why I decided to change my idea to something that involves a smaller device that makes small sounds and is easily accessible by the user. 

The other main piece of feedback followed a similar idea, but was more general. It was that the device in my video would likely set off the alarm when someone leaves the fridge open just to grab something else from the kitchen, like most people do at some point. Because of those two things, I decided it would be best if I tried a new idea for Part B of this lab.

## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors! Again, be creative!
3) We will be grading with an emphasis on creativity. 

\*\***Document everything here. (Particularly, we would like to see the storyboard and video, although photos of the prototype are also great.)**\*\*

For Part B of this lab, I decided to change my idea of what to design an interaction of. Instead of doing an alarm that reminds the user when it is left open, I decided to instead model a smart wearable bracelet that tracks misses and makes while shooting a basketball. 

The device works by using a sensor on the hoop that detects makes and misses and then making a dissatisfying noise. This noise serves as a signifier that the miss registered. Contrarily, it also makes a satisfying sound when the ball goes in the hoop. The bracelet has a display on it that shows the player's stats for this shooting session, in the form of how many shots the user has made over the total number of shots the user has attempted.

The reasoning for switching is that I did not see too much room for innovation or improvement in terms of the video-making of the previous idea. This one has the potential for mimicking sound notifications and a changing display.

Here is the video of the final demonstration:

[![Watch the video](https://img.youtube.com/vi/7YinQY9AZ28/0.jpg)](https://www.youtube.com/watch?v=7YinQY9AZ28)


The thumbnail of this video (image that links to the video above) is what the prototype bracelet looks like. I made it using a bracelet and sticking a circular cut of paper onto it using tape. 
