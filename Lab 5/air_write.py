import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
import alsaaudio
#import imutils
m = alsaaudio.Mixer()
################################
wCam, hCam = 640, 480
################################
 
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
 
detector = htm.handDetector(detectionCon=0.7)
minVol = 0
maxVol = 100
vol = 0
volBar = 400
volPer = 0

success, old_frame = cap.read()
#old_frame = imutils.resize(old_frame,
mask = np.zeros_like(old_frame)

prev = False
pinch = False
cx, cy = (0, 0)
prev_x, prev_y = (0,0)
state = 0 # 0 for normal, 1 for transitioning to drawing, 2 for drawing

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
 
        thumbX, thumbY = lmList[4][1], lmList[4][2] #thumb
        pointerX, pointerY = lmList[8][1], lmList[8][2] #pointer

        middleX, middleY = lmList[12][1], lmList[12][2]
        ringX, ringY = lmList[16][1], lmList[16][2]
        pinkyX, pinkyY = lmList[20][1], lmList[20][2]
        
        cx, cy = (thumbX + pointerX) // 2, (thumbY + pointerY) // 2
 
        #cv2.circle(img, (thumbX, thumbY), 15, (255, 0, 255), cv2.FILLED)
        #cv2.circle(img, (pointerX, pointerY), 15, (255, 0, 255), cv2.FILLED)
        #cv2.circle(img, (middleX, middleY), 15, (255, 0, 255), cv2.FILLED)
        #cv2.circle(img, (ringX, ringY), 15, (255, 0, 255), cv2.FILLED)
        #cv2.circle(img, (pinkyX, pinkyY), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (thumbX, thumbY), (pointerX, pointerY), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        len_calc = lambda x1,y1,x2,y2: math.hypot(x2 - x1, y2 - y1)
        length = len_calc(thumbX,thumbY,pointerX,pointerY)
        length1 = len_calc(pointerX,pointerY,middleX,middleY)
        length2 = len_calc(middleX, middleY, ringX, ringY)
        length3 = len_calc(ringX, ringY, pinkyX, pinkyY)
        length4 = len_calc(thumbX,thumbY, ringX, ringY)
        print(length1,length2,length3)
        condition = length>100 and length1>100 and length2<100 and length3>100 and length4<100
        #if condition:
        #    m.setvolume(0)
        #    volPer = 0
        #    volBar = 400
        #    print("CONDITION")
        #    cv2.putText(img, 'quiet coyote!', (40, 70), cv2.FONT_HERSHEY_COMPLEX,
        #        1, (255, 255, 255), 3)
        #else:
# 
        #    vol = np.interp(length, [50, 300], [minVol, maxVol])
        #    volBar = np.interp(length, [50, 300], [400, 150])
        #    volPer = np.interp(length, [50, 300], [0, 100])
        #    m.setvolume(int(vol))

        #print(int(length), vol)

 
        if length < 50:
            pinch = True
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED) 
        else:
            pinch = False
    
    if pinch==True and prev==False: # Transitioning
        state = 1
    elif pinch==True and prev==True: # Drawing
        state = 2
    else: # Normal
        state = 0
    
    if state==0:
        cv2.putText(img, 'Pinch to draw!', (40,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    elif state==1 or state==2:
        cv2.putText(img, 'Move pinch to draw!', (40,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    else:
        print('Unattainable state')

    if state==2:
        mask = cv2.line(mask, (prev_x,prev_y),(cx,cy), (255,0,255), 3)
    
    prev = pinch
    prev_x, prev_y = (cx, cy)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    #cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
    #            1, (255, 0, 0), 3)
 
    img = cv2.add(img, mask)
    cv2.imshow("Img", img)
    cv2.waitKey(1)
