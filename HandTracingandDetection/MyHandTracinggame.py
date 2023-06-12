import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    # Read a frame from the camera
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=True)
    if len(lmList) != 0:
        cv2.circle(img, (lmList[4][1], lmList[4][2]), 15, (255, 0, 0), cv2.FILLED)
        cv2.putText(img,f"4",(lmList[4][1], lmList[4][2]),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),2)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img,f'FPS: {int(fps)}',(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),4)
    # Display the frame in a window
    cv2.imshow('Image', img)

    # Wait for a key press and check if the user wants to quit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()