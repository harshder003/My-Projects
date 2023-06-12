import cv2
import numpy as np
import time
import sys
sys.path.append('D:\My Projects\PoseEstim')
import PoseEstModule as pm

cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
dir = 0
while True:
    success, img = cap.read()
    img = detector.findPose(img, draw = True)
    lmList = detector.getPosition(img, draw = True)
    # angle = detector.findAngle(img, 11, 13, 15)

    if len(lmList) != 0:
        angle = detector.findAngle(img, 12, 14, 16)
        per = np.interp(angle, (200, 320), (0, 100))
        bar = np.interp(angle, (200, 320), (400, 150))
        # print(angle, per)
        # Check for the dumbbell curls
        color = (255, 0, 255)
        if per == 100:
            if dir == 0:
                dir = 1
                count += 0.5
                # print(count)
        if per == 0:
            if dir == 1:
                dir = 0
                count += 0.5
                # print(count)
            color = (0, 255, 0)
            cv2.putText(img, 'Curl', (50, 150), cv2.FONT_HERSHEY_PLAIN, 3, color, 3)
        cv2.rectangle(img, (50,150), (85,400), (0,255,0), 3)
        cv2.rectangle(img, (50,int(bar)), (85,400), (0,255,0), cv2.FILLED)
        cv2.putText(img, f'Count:{int(count)}', (40, 450), cv2.FONT_HERSHEY_PLAIN, 2, color, 3)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
