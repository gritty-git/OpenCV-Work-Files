import numpy as np
import cv2
img=cv2.imread("opencv1.jpeg",-1)
green_low=np.array([0,157,0])
green_high=np.array([127,255,167])
mask=cv2.inRange(img,green_low,green_high)
cv2.imshow("mask",mask)
res=cv2.bitwise_and(img,img,mask=mask)
res[np.where((res==[0]).all(axis=2))]=[255]
cv2.imshow("res",res)
cv2.imwrite("green1.jpg",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
