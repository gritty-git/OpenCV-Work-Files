import numpy as np
import cv2
im=cv2.imread("a4c.png", 1)
img=cv2.imread("a4c.png", cv2.IMREAD_GRAYSCALE)
_,threshold= cv2.threshold(img,70,255,cv2.THRESH_BINARY)
font=cv2.FONT_HERSHEY_COMPLEX

rng = cv2.selectROI(im)
#Here we select the range for shape dedection
print(rng)
imcrop = im[int(rng[1]) : int(rng[1] + rng[3]), int(rng[0]) : int(rng[0] + rng[2])]
#Here we take image from selected range

thresh = 20 # we approx the threshold value

bmin = imcrop[:, :, 0].min()
gmin = imcrop[:, :, 1].min()
rmin = imcrop[:, :, 2].min()
#Lower bound for threhold

bmax = imcrop[:, :, 0].max()
gmax = imcrop[:, :, 1].max()
rmax = imcrop[:, :, 2].max()
#Upper bound for threshold
print(bmax,gmax,rmax)
bgrmin = np.array([bmin - thresh, gmin - thresh, rmin - thresh])
bgrmax = np.array([bmax + thresh, gmax + thresh, rmax + thresh])
#Minus and plus are just for good thrsholding, thresh == 20 is not fix we change as we need

threshold = cv2.inRange(im, bgrmin, bgrmax)
cv2.imshow("threshold",threshold)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    approx=cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True),True)
    cv2.drawContours(img,[approx],0,(255),2)
    if len(approx)==3:
        print(approx.ravel())
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        cv2.putText(im,"Triangle",(x,y),font,0.5,(255,255,255))
    elif len(approx)==4:
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        cv2.putText(im,"Square",(x,y),font,0.5,(255,255,255))
    elif len(approx)==5:
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        cv2.putText(im,"Pentagon",(x,y),font,0.5,(255,255,255))
    elif len(approx)==6:
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        cv2.putText(im,"Hexagon",(x,y),font,0.5,(255,255,255))
    elif len(approx)>=7:
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        cv2.putText(im,"Circle",(x,y),font,0.5,(255,255,255))
cv2.imshow("img", img)
cv2.imshow("Threshold",threshold)
cv2.imshow("im",im)
cv2.waitKey(0)
cv2.destroyAllWindows()
