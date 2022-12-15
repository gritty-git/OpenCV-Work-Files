import numpy as np
import cv2
img=cv2.imread("2.jpg",1)
cv2.line(img,(0,0),(604,439),(128,128,128),11)
cv2.rectangle(img,(5,5),(505,334),(0,0,255),6)
cv2.circle(img,(302,219),50,(255,0,0),-1)
pts=np.array([[12,12],[12,112],[112,112],[112,12]])
cv2.polylines(img,[pts],True,(255,255,0),8)
cv2.imshow("window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
