import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while True:
    res,fframe=cap.read()
    frame=np.flip(fframe,axis=1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red=np.array([0,0,0])
    upper_red=np.array([15,255,255])
    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    k=cv2.waitKey(2)
    if k==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
