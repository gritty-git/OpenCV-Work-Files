import numpy as np
import cv2
img1=cv2.imread("book.jpg",-1)
cv2.imshow("book",img1)
ret,thresh=cv2.threshold(img1,20,255,cv2.THRESH_BINARY)
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret2,graythr=cv2.threshold(gray,20,255,cv2.THRESH_BINARY)
top=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,4)
cv2.imshow("jatra",thresh)
cv2.imshow("Gray",graythr)
cv2.imshow("Top",top)
cv2.waitKey(0)
cv2.destroyAllWindows()
