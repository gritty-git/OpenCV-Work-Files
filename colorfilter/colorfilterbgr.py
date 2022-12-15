import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while True:
    res,fframe=cap.read()
    frame=np.flip(fframe,axis=1)
    lower_red=np.array([0,0,10])
    upper_red=np.array([255,255,255])
    pmask=cv2.inRange(frame,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=pmask)
    cv2.imshow("frame",frame)
    cv2.imshow("pmask",pmask)
    cv2.imshow("res",res)
    k=cv2.waitKey(2)
    if k==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
