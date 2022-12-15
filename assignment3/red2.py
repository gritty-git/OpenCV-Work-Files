import numpy as np
import cv2
img=cv2.imread("opencv2.png",-1)
red_low=np.array([0,0,127])
red_high=np.array([125,125,255])
mask=cv2.inRange(img,red_low,red_high)
cv2.imshow("mask",mask)
res=cv2.bitwise_and(img,img,mask=mask)
res[np.where((res==[0]).all(axis=2))]=[255]
cv2.imshow("res",res)
cv2.imwrite("red2.jpg",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
