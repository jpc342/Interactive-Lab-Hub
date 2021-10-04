# Interactive Prototyping: The Clock of Pi

Does it feel like time is moving strangely during this semester?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

**Please indicate anyone you collaborated with on this Lab here.**

I worked with Bella Baidak (bb568) for this lab. Also, we took inspiration from the website https://climateclock.world/.

## Prep

[Lab prep](prep.md) is extra long this week! Make sure you read it over in time to prepare for lab on Thursday.

### Get your kit

### Set up your Lab 2

## Overview
For this assignment, you are going to 

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the \*\*\***stars**\*\*\*. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

## Part A. 
### Connect to your Pi


## Part B. 
### Try out the Command Line Clock


## Part C. 
### Set up your RGB Display

### Hardware (you have done this in the prep)

### Testing your Screen

#### Displaying Info with Texts

#### Displaying an image


## Part D. 
### Set up the Display Clock Demo

### How to Edit Scripts on Pi

## Part E.
### Modify the barebones clock to make it your own

**We strongly discourage and will reject the results of literal digital or analog clock display.**

\*\*\***A copy of your code should be in your Lab 2 Github repo.**\*\*\*

A copy of my code is in the file "screen_clock2.py" in this repository. I added code inside and outside the while loop in order to create the clock described below.

## Part F. 
## Make a short video of your modified barebones PiClock

We decided to make an environmental awareness clock. It may not be incredibly useful for telling the current the time, but it does show the world climate clock, which shows by what day we need to be net zero emissions at the current rate of climate change. We decided to also include an interactive element to it, which includes having a line of text telling the user to press the button to see tips for them to personally help out the environmental cause. By pressing this button multiple times, it randomly cycles through tips like "Use reusable water bottles" that the user can remind themselves of to do their part. Here is the video of its usage:

\*\*\***Take a video of your PiClock.**\*\*\*

[![Watch the video](https://img.youtube.com/vi/Yjg8sS0PzSI/0.jpg)](https://www.youtube.com/watch?v=Yjg8sS0PzSI)

## Part G. 
## Sketch and brainstorm further interactions and features you would like for your clock for Part 2.

Here is the brainstorm we had for the next iteration of this clock.

![image](https://user-images.githubusercontent.com/67603876/134106198-1fa88089-20f2-4fd1-934b-f7540c6923e6.png)

One other thing we might like to add is something that counts up in order to help actually tell time in a useful way to the user, which might be in other environmental terms like plastic wasted per minute, etc.

# Prep for Part 2

1. Pick up remaining parts for kit.

2. Look at and give feedback on the Part G. for at least 2 other people in the class (and get 2 people to comment on your Part G!)

# Lab 2 Part 2

Pull Interactive Lab Hub updates to your repo.

Modify the code from last week's lab to make a new visual interface for your new clock. You may [extend the Pi](Extending%20the%20Pi.md) by adding sensors or buttons, but this is not required.

As always, make sure you document contributions and ideas from others explicitly in your writeup.

You are permitted (but not required) to work in groups and share a turn in; you are expected to make equal contribution on any group work you do, and N people's group project should look like N times the work of a single person's lab. What each person did should be explicitly documented. Make sure the page for the group turn in is linked to your Interactive Lab Hub page. 

Some feedback we got is that our clock may not be the best for actually telling time; however, we did not address this feedback because telling time is not the purpose of our clock. Another piece of feedback we recieved is that it would be nice to see the 0 emmisions deadline clock alone on a seperate screen; this was a great suggestion and we added it in our new display!

For the updates to our display we added a new screen displaying the 0 emisions deadline clock alone. We also incorporated the joy stick as a new piece of hardware. When on the tip screen if you swipe up or down with the joy stick a new tip on how help reach 0 emissions will be displayed. When you moved the joy stick horizontally it switches between the tip screen and just the 0 emission clock screen.

To get the joystick working we used Qwiic Joystick Py libary from Github. The code for the clock is included in the screen_clock4.py file in this folder.

Check out our updates in this video:

[![Watch the video](https://img.youtube.com/vi/RkIFK3NXVbI/0.jpg)](https://www.youtube.com/watch?v=RkIFK3NXVbI)
