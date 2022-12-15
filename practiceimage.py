import cv2
image=cv2.imread("opencv1.jpeg",-1)
cv2.imshow('window',image)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)
f=cv2.waitKey(0)
print(f)
cv2.destroyAllWindows()
