import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('free.mkv')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('original',frame)
    cv2.imshow('fg',fgmask)

    k=cv2.waitKey(2)
    if k==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
