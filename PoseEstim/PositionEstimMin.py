import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture(0)

pTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    for id, lm in enumerate(results.pose_landmarks.landmark):
        h,w,c = img.shape
        cx,cy = int(lm.x*w),int(lm.y*h)
        cv2.putText(img,f"{id}",(cx,cy),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),2)
        cv2.circle(img, (cx, cy), 5, (0, 255, 255), cv2.FILLED)
    mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img,f'FPS: {int(fps)}',(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),4)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()