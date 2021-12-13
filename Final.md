# The Tail of Two Kitties

## Project Description

This project consists of two interactive kitties that respond in cat-like ways when touched by the user. When interacted with through petting, the cats purr, wag their tails, move their paws, and meow. These two cats are also connected. When both cats are being interacted with at the same time a heart light will turn on, on both the cats and the cats will meow. The goals of this project are to create an emotional experience for users similar to petting a cat and to connect long distance friends through interacting with our cats.

The inspiration for this project comes from our feelings and the feelings of the people surrounding us during the pandemic. During this time and especially during quarantine, we saw that people were feeling trapped in their homes with nothing to do and, more importantly, isolated from people they care about. In response to this, a lot of people decided to get dogs, cats, or other pets to try to fill that void, but there are two problems with this. The first is that not everyone is able to get a pet due to cost, allergies, or other reasons, and the second is that this does not change the fact that people have been separated from their loved ones. We wanted to try and fix these problems with robotic pets that are individually interactive, but that are also connected so that people that are geographically separated can be connected in a way that feels organic. 

We were also very much inspired by the research of Ran Zhou that highlights an emotional response in users from robotic physical contact (https://www.ranzhourobot.com/).

[add story board]

## Design Process

To create these two cats we used the following technology:
- Raspberry Pi
- Capacitive touch sensors
- Servo motors
- MQTT communication
- Speakers
- LED Light

The appearance of the cats was made up of:
- Cardboard
- A furry sweater
- Conductive tape
- Wire
- Yarn
- Ribbon

To start building these two cats, we first created a simple 2D cardboard verison of the cats to test the technology would work well together and to prototype user interaction. The 2D verison of the cats used the servo motor to move a cardboard arm of the cat when it is touched. The 2D cats also purr when they are touched, and they show the connection between the two cats by shining a red LED light through a paper heart when both are interacted with at the same time.

This is what the 2D cats look like:

<img width="975" alt="Screen Shot 2021-12-12 at 10 27 58 PM" src="https://user-images.githubusercontent.com/73661058/145747859-02a0b7d6-1545-4ae9-8d12-89e53d377581.png">

One cat working:

https://user-images.githubusercontent.com/73661058/145748293-b33c4179-f564-44e3-8904-8b506f14eace.mov

Two cats working together:

[Soul insert your video here]

Back view of the cats:

<img width="546" alt="Screen Shot 2021-12-12 at 10 29 19 PM" src="https://user-images.githubusercontent.com/73661058/145747959-8223169d-07ca-407b-9071-c8cad17d4071.png">

To make this technology work, we had to integrate several different functions into the program because a making something "interactive" almost by definition means there must be more than one type of action from the user to start an interaction and more than one type of reaction from the device in response. For each individual cat, we used capacitive sensors, speakers, servo motors, and MQTT communication. Here is a diagram of the full system architecture:

![image](https://user-images.githubusercontent.com/67603876/145860922-fc8fa2b2-c298-4d65-b751-c4fdadccd171.png)

The interactions alone have all individually been done before in previous labs, so integrating them was the biggest technological challenge. Since there were so many things connected and running at the same time, it was easy for us to miss something being slightly unplugged or for the Raspberry Pi to miss when one of the sensors was touched, so we ran into a lot of Remote I/O errors while prototyping. Additionally, the connection to the MQTT server would drop on occasion, which we mainly worked around by restarting the program, and this seemed to work.

As seen in the above images, the capacitive touch sensors were connected by alligator clips to rectangular conductive strips that we made by cutting up a soda can, which we thought would be ideal because they are thin and light, while also being easy to clip onto and tape down, as well as being conductive. We would use this same method of spreading out the touchable areas of the sensors in the final design of the cat, until we ran into some problems, which will be discussed later. Regardless, these "touch pads" worked well for the prototype, and the other functions did not cause many issues.

After validating that all of our technological components worked well together and testing the interactions of our 2D cats with some peer users we began constructing the 3D cats. Our plan to create these 3D cats was to created a cardboard skeleton for the cats, place wires for sensors and servo motors in the skelton and cover the cardboard skelton with fur to give a cat like appearance and feel. In our user testing, we found that people loved the idea of the interactive robotic pet, but the unrealistic look of the 2D prototype was certainly a factor in making the experience more artificial than it should be. For this reason, we knew we had to really create a realistic-enough looking cat and find a way to integrate our technology into it; otherwise, our final product would not have the desired effect of bringing people comfort.

To create the cats cardboard skelton, we found some 3D model puzzles online and used to a laser cutter to cut them pieces. This process took us much time and experimentation. The first cat 3D model puzzles we found looked nice but when cut there was way too many pieces and we struggled to put it together. This lead us to finding a new model with less pieces that was more managable for our project. Once we selected our model we had to experiment with cardboard thickness to find the best possible skeltons for our kitties.

Complicated cat 3D model puzzle:

<img width="548" alt="Screen Shot 2021-12-12 at 10 56 34 PM" src="https://user-images.githubusercontent.com/73661058/145750070-ba868da3-1f17-4aed-983a-bf56a8d5b873.png">

Simpler cat 3D model puzzle we used:

![IMG_7064](https://user-images.githubusercontent.com/73661058/145750078-69435904-f33b-41a9-aba5-3f87c68b9e88.jpg)

Once we had our cardboard skeletons created, we added in the servo motors and tested out the movement of our kitties as skelton cats. Our design is built around a few central frame pieces, so to get our servos to be in the right spots, we had to attach them to one of those central pieces. This was done easily with tape (instead of glue to avoid complications of glue directly on electronics), but the motors are slightly too large to fit between two central pieces in our puzzle piece model. To fix this, we cut holes in the next piece over so that the motors would just fit through them without messing up the structural integrity of the cat. There were two servo motors per cat that had to be attached, one at the arm and one at the tail. 

As seen in the image directly above, the edge piece of the cardboard model includes both left legs in one piece (we call the front leg the "arm" for simplicity's sake). Consequentely, we first detached the arm of the cat from that edge piece of the model so that it could be moved separately from the left leg. We then cut a gap in the skeleton as mentioned above to place the motor. We also had to cut a small hole in the original piece that held the arm because just the small part of the motor that holds the moving attachment had to poke through. Lastly, we hot glued the detached cat arm to the attachment of the motor, so that the arm can move on its own outside the stationary frame, giving the illusion of a shoulder joint. For the tail's motor, we started by completely removing the cardboard tail that was part of the original model, and we replaced it with a more realistic looking tail, which consisted of yarn wrapped around a wire to hold its shape. Then, we placed the motor in a similar way to the arm motor, and that was enough for the tail to work.

Photos of this stage:

<img width="829" alt="Screen Shot 2021-12-12 at 11 09 28 PM" src="https://user-images.githubusercontent.com/73661058/145751091-66acae65-2b39-4e8b-8f7c-f1fc218a6c93.png">
<img width="556" alt="Screen Shot 2021-12-12 at 11 09 58 PM" src="https://user-images.githubusercontent.com/73661058/145751120-eb435b79-7ca3-4506-8318-b09975b34ad5.png">

Next we added the same conductive strips that were used in the 2D model to the 3D skeleton for the touch sensors, which we attached to alligator clips that ran through the skeleton out the bottom. Before doing this, we did some testing with these strips because our plan was to put these sensors underneath the fur of the cat because they are capacitive, so we thought they may work. To test this, we just tried putting different types of materials, as well as the fur we chose (details discussed later) on top of the strips and seeing if we could just sense a touch. During our testing, this seemed to work with no problems, so after we were convinced that it would work, we went through with the plan. While it did work at first after the fur was put on and everything, at some point, the touch sensors completely stopped working under the fur, and the only way to trigger them after this point was HERR

covered the skeltons in furr. For the cat furr we used an old sweater we thrifted from GoodWill. To get a cat shape from the furr we first created a pattern with thinner fabric and then cut it out of the thick furr material. Lastly, we hot glued the furr coat on to the cat skeltons.
Fabric pattern for furr:

<img width="542" alt="Screen Shot 2021-12-12 at 11 31 00 PM" src="https://user-images.githubusercontent.com/73661058/145752752-78581013-b9c8-45e8-9572-f4337c93e5a9.png">
<img width="551" alt="Screen Shot 2021-12-12 at 11 31 39 PM" src="https://user-images.githubusercontent.com/73661058/145752815-ab649266-ac61-4278-8fc2-e5c512987300.png">
<img width="553" alt="Screen Shot 2021-12-12 at 11 32 16 PM" src="https://user-images.githubusercontent.com/73661058/145752843-591fb3e4-3495-4e68-9346-fa541159cbaf.png">

Cat covered in furr:

<img width="529" alt="Screen Shot 2021-12-12 at 11 32 57 PM" src="https://user-images.githubusercontent.com/73661058/145752889-6070a3bf-a233-4c88-8f0a-3ef64048f2d8.png">

[Add more details here and any more photos you have]

The last step to the cats appearance was to add the heart light for interaction between the two cats. To do this we taped the LED lights to the chest of the cats, covered them in a thin furr to intensify thier shine, and put a duct tape heart on top of the chest furr.

Heart light:

<img width="509" alt="Screen Shot 2021-12-12 at 11 33 32 PM" src="https://user-images.githubusercontent.com/73661058/145752955-b879156c-d9de-4477-85e1-e24a95d62769.png">

Under the cats we added a box for cat to stand on. This served to stablize the cat allowing it to stand and hide the pi, senors, and speaker from the user.

[Discuss more about the cats stand and box if necessary]
[In general add any photos or details I missed from this section]

## Final Device Design
Final look:

<img width="528" alt="Screen Shot 2021-12-12 at 11 39 15 PM" src="https://user-images.githubusercontent.com/73661058/145753356-41e7d3c1-1dbd-4fe7-8f7a-37ed99b667da.png">

Evolution of the cats:

<img width="987" alt="Screen Shot 2021-12-12 at 11 40 52 PM" src="https://user-images.githubusercontent.com/73661058/145753486-5a504150-8990-4678-a394-a148412aaba7.png">

Cats working:

https://user-images.githubusercontent.com/73661058/145753313-f118803b-0259-4138-ba82-10a24565e6ff.mov

Us with the cats :blush: :

<img width="517" alt="Screen Shot 2021-12-12 at 11 40 29 PM" src="https://user-images.githubusercontent.com/73661058/145753457-aa2a2e7b-e35a-41ef-ba3f-67a6326bb5cb.png">

[Add any more photos for photos and videos]
[any comments about peoples reactions and interacts with the cats ]
