import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(True):
    _,frame=cap.read()
    frame=np.flip(frame,axis=1)

    yellow_low = np.array([0, 127, 127])
    yellow_high = np.array([127, 255, 255])
   
    threshold = cv2.inRange(frame, yellow_low, yellow_high)
    
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        cv2.drawContours(frame, [approx], 0, ([0,0,255]), 6)
    cv2.imshow('Window', frame)
    cv2.imshow('threshold', threshold)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

