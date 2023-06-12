import cv2
import time
import numpy as np
import sys
sys.path.append('D:\My Projects\HandTracingandDetection')
import HandTrackingModule as htm
import math

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

cap = cv2.VideoCapture(0)

###Webcam properties###
wCam, hCam = 640, 480

cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    # volume.GetMute()
    # volume.GetMasterVolumeLevel()
    (minVol,maxVol,w) = volume.GetVolumeRange()

    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        x1,y1 = lmList[4][1], lmList[4][2]
        x2,y2 = lmList[8][1], lmList[8][2]
        cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (lmList[8][1], lmList[8][2]), 10, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (255,0,255), 3)
        cx,cy = (x1+x2)//2, (y1+y2)//2
        cv2.circle(img, (cx,cy), 5, (255, 0, 255), cv2.FILLED)
        length = math.hypot(x2-x1,y2-y1)
        cv2.putText(img,f'Length: {int(length)}',(10,140),cv2.FONT_HERSHEY_PLAIN,3,(0,255,255),4)
        if length < 25:
            cv2.circle(img, (cx,cy), 5, (0, 255, 0), cv2.FILLED)
        # Len range 50 - 300
        # Volume range -96 - 0
        vol = np.interp(length,[10,250],[minVol,maxVol])
        volume.SetMasterVolumeLevel(vol, None)
        volBar = np.interp(length,[10,250],[400,150])
        cv2.rectangle(img, (50,150), (85,400), (0,255,0), 3)
        cv2.rectangle(img, (50,int(volBar)), (85,400), (0,255,0), cv2.FILLED)
        pervol = np.interp(length,[10,250],[0,100])
        cv2.putText(img,f'Vol: {int(pervol)}%',(10,100),cv2.FONT_HERSHEY_PLAIN,3,(0,255,255),4)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img,f'FPS: {int(fps)}',(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,255),4)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        volume.SetMasterVolumeLevel(0, None)
        break

cap.release()
cv2.destroyAllWindows()