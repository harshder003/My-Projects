import cv2
import mediapipe as mp
import time
import PoseEstModule as pm

cap = cv2.VideoCapture(0)
pTime = 0
detector = pm.poseDetector()
while True:
    success, img = cap.read() 
    img = detector.findPose(img)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img,f'FPS: {int(fps)}',(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),4)
    lmList = detector.getPosition(img)
    if len(lmList) != 0:
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 5, (255, 0, 0), cv2.FILLED)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        break