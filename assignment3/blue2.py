import numpy as np
import cv2
img=cv2.imread("opencv2.png",-1)
blue_low=np.array([127,0,0])
blue_high=np.array([255,167,127])
mask=cv2.inRange(img,blue_low,blue_high)
cv2.imshow("mask",mask)
res=cv2.bitwise_and(img,img,mask=mask)
res[np.where((res==[0]).all(axis=2))]=[255]
cv2.imshow("res",res)
cv2.imwrite("blue2.jpg",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
