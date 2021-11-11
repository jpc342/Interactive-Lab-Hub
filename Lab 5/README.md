# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms needs to be aware of.

## Prep

1.  Pull the new Github Repo.
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2021/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:

1. Raspberry Pi
1. Webcam 
1. Microphone (if you want to have speech or sound input for your design)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

Following is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

Contours:

![Contours](https://user-images.githubusercontent.com/67603876/140829420-de788b71-650c-4229-b9b8-6ae4cedb53bc.PNG)

One application that could take advantage of what Contours does is one that detects handwriting. The contours could be used to discover the edges of writing. One potential application of this could be to have glasses or some sort of headwear that watches as the user takes notes on a notebook, then automatically uses contours to do some kind of edge detection. This would make the edges of the writing clearer, so that it would be easier to to determine what the letters say automatically.

Face detection:

![Face-detection](https://user-images.githubusercontent.com/67603876/140829500-292ff6dc-0678-4c59-8b6e-8586b85b88d7.PNG)

A design that might use this well is a webcam on a computer that detects faces, and (if it were a little more accurate this would work better) when the user starts to drift off into sleep, it would detect that flickering or shutting of the eyes and tell the user to go to sleep or get off the computer.

Optical flow:

![Optical-flow](https://user-images.githubusercontent.com/67603876/140829531-ea9d8d78-0c06-4c71-8f5a-9d2a3c87c0fe.PNG)

An application that would use this effectively is a form-tracker that can help a user analyze their form while performing some action. This could be tracking their feet while running, their hands while shooting a basketball, or other things where the specific motion and trajectory of a body part are very important.

Object detection:

![Object-detect](https://user-images.githubusercontent.com/67603876/140829515-330cb63d-3412-4e62-bac4-15b276993db9.PNG)

One design that could use this effectively is to have an overhead camera that monitors either the floor, a table, or counterspace, and when there are "too many" objects lying there, it would remind the user to clean up, so that things do not pile up.

#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi4 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

![Hand-pose](https://user-images.githubusercontent.com/67603876/140834543-d4ef348d-5803-4feb-8e24-0855c33d5bfd.PNG)

This position based approach gives us the opportunity to create interactions that are AR/VR-like. Detection of the hand can create the possibility of being able to control things like music volume, viewing and moving images that overlay on the reality that the user sees. The pinching can be used to "pick up" or select objects in order to move them, open menus, or just track one point around the screen (that last application could be used for something like writing on your reality with a virtual pen, where when the user pinches, the pen starts drawing, and when the user stretches their fingers back out, the pen stops drawing).

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)


#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***

Here is the program's output when I am not wearing a mask:

![PPE1](https://user-images.githubusercontent.com/67603876/140838148-92ffe05e-30b7-4ea4-ae69-3e7f42e91d34.PNG)

Then, I put on a mask, and here was the new output:

![PPE2](https://user-images.githubusercontent.com/67603876/140838156-b0a4cd62-0212-4037-8e01-cbb3d29e4382.PNG)

Teachable Machines offers unique capabilities to train and retrain the model on new data. Not only can this be used for the obvious use of the ppe_detection one where the a camera can be used to detect if people are wearing masks or not, but this type of Teachable Machine can be used to do things like detect what comes up to, for example, someone's front door in view of a security camera. This can provide classification capabilites, which is much less available and easy with OpenCV or MediaPipe.

*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


#### Filtering, FFTs, and Time Series data. (optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.


### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

I have decided to pick the MediaPipe hand pose model. 

Two interactions I am considering making are 
- (1) a virtual piano, which plays notes based on what fingers the user moves instead of where they are placed. In this case, the user would simply put their hands on camera and have ten notes (one for each finger) available to play based on if those fingers make the motion of playing a piano key. The problem here is that the user would need to be able to move each finger individually without much motion in other fingers, which, especially for the ring finger for most people, is very difficult.
- (2) a tool that can help a user write and draw virtually on any surface in an augmented reality sort of way. In this case, the user would wear the camera in some way, perhaps with a AR headset or with a camera built into a hat, and use the pinching function to denote where to draw on the video of their surroundings. The difficulty here will likely be making the program smooth enough to handle drawings so that they are still easily discernable and not cluttered and blocky.

In order to decide, I thought about which one was more feasible. I tried to design a camera mount that would make it easier to see which fingers are moving the most, but the camera angle that allows me to do this (parallel with the surface the hands are resting on) does not allow a good enough view of the hands for the program to find them. I figured it would be easier to instead build something like a glasses frame that houses the camera like Google Glass and to do the drawing, since pinch detection is doable as shown in one of the given example. 


### Part C
### Test the interaction prototype

I tested this by attaching the camera to a prop crown I had lying around and keeping a rectangular tape boundary on a table which represents the camera's field of view. When the user pinches I start mimicking their drawing on a physical "camera feed." 

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
   The system succeeds when the user is slow and deliberate with their drawings, and when they keep in mind where the boundaries for their hands are.
2. When does it fail?
   The system fails when the user moves their hands too fast, or loses track of where their hands are by looking at the camera feed instead of their hands.
3. When it fails, why does it fail?
   It fails because the system (me in the tests) is not fast enough to handle sudden movements, and the camera has a fixed zoom and range.
4. Based on the behavior you have seen, what other scenarios could cause problems?
   Other scenarios that could cause problems are when the user's hands cross or are at angles that make it hard for the camera (me in the testing) to see whether or not they are pinching or not.

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
   No, the user would not be aware right away of the capabilities and shortcomings of the system, like the hand detection not being as good close to the edges than in the middle, etc.
2. How bad would they be impacted by a miss classification?
   The worst thing that could happen is a false-positive sign of a pinch and start drawing an errant line where there is not supposed to be one.
3. How could you change your interactive system to address this?
   Adding instructions on screen would only clutter it, and it would hide some of the video feed which is very important to have. One thing I could consider for this is an eraser function.
4. Are there optimizations you can try to do on your sense-making algorithm?
   I can try to delete as many extraneous commands and statements in the code to try and speed up the framerate as much as possible so that the drawing is as smooth as possible. With how the hand detection algorithm works and the processing power of the Raspberry Pi, though, I am not sure it will be able to get to a market-level smoothness.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
  AirWrite can be used for making small notes and drawing things seemingly on top of the surfaces around the user.
* What is a good environment for X?
  A good environment for AirWrite is on a video call, where the camera is built into the device. Another would be a livestream or tutorial video for a hands-on task, where the person making the video can make marks and notes with their hands while doing something to better point out things they look for.
* What is a bad environment for X?
  A bad environment for AirWrite is in situations where someone is trying to take a lot of notes quickly, like for a student. That is not what this system is built for.  
* When will X break?
  In the above situations, also when the hand nears the edges of the screen.
* When it breaks how will X break?
  It will make mistakes if the hand moves too fast, or if there is too much writing on screen, it will appear too cluttered.
* What are other properties/behaviors of X?
* How does X feel?
  AirWrite feels like a fun tool, not extremely efficient, but like something to enhance virtual conversations.

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

Application without the physical prototype:

[![Watch the video](https://img.youtube.com/vi/99mF6zps-qk/0.jpg)](https://www.youtube.com/watch?v=99mF6zps-qk)

Clearly, the writing is somewhat slow, so that is why I defined the best and worst environments as above. 

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***

The code for this project can be seen in the file air_write.py. Here is the video of it working:

[![Watch the video](https://img.youtube.com/vi/wKl5hLVCYLA/0.jpg)](https://www.youtube.com/watch?v=wKl5hLVCYLA)

The different applications shown in the video above show some of the good applications of AirWrite. Some of the notes written are things that could be part of a FaceTime call between the user and someone else when they want to either draw something or help the other understand if their hearing is impaired in any way. Another application shown is a rough rendition of what a virtual tutoring/teaching session could look like with AirWrite. 

In terms of prototyping this design, my original intent was to use a cut out of a frame of glasses to mount the webcam onto and hide the wire behind it. However, the webcam we are using was far too bulky to fit into the frame or just not dig into the skin of the user. It also weighs too much to wear on one's nose like that. Instead, I chose to insert it into a hat, to mimic a GoPro camera setup. This design would make sense more for the virtual first-person teaching session than for the FaceTime application. However, the main thing I wanted to get out of this was to see how people interacted with the actual writing, which this way of prototyping it works fine for.

Future work: Some of the feedback I got on this design (some from before the second part and some after) included that I should build in an eraser functionality to the opposite hand or to a different hand gesture. Another related design flaw is that those who used this noted there is no "clear" button anywhere to clear all text from screen or undo an errant stroke with the AirWrite pen. One other thing mentioned was that when "writing" while standing and looking forward instead of sitting looking down, the user has to extend their arms almost fully out, which makes it difficult to keep their arms still. 


