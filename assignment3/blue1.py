import numpy as np
import cv2
img=cv2.imread("opencv1.jpeg",-1)
blue_low=np.array([127,0,0])
blue_high=np.array([255,197,117])
mask=cv2.inRange(img,blue_low,blue_high)
cv2.imshow("mask",mask)
res=cv2.bitwise_and(img,img,mask=mask)
res[np.where((res==[0]).all(axis=2))]=[255]
cv2.imshow("res",res)
cv2.imwrite("blue1.jpg",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
