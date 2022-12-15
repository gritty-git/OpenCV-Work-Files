import numpy as np
import cv2
img=cv2.imread("2.jpg",-1)
img[100:150,100:150]=[255,0,255]
cv2.imshow("window",img)
bird=img[87:247,87:247]
img[0:160,0:160]=bird
cv2.imshow("window2",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
