import cv2
import numpy as np

cap = cv2.VideoCapture(0)
red_low = np.array([0, 0, 127])
red_high = np.array([50, 50, 255])
green_low = np.array([0, 127, 0])
green_high = np.array([127, 255, 127])
blue_low = np.array([127, 0, 0])
blue_high = np.array([255, 127, 127])
yellow_low = np.array([0, 127, 127])
yellow_high = np.array([50, 255, 255])
while True:
    _, fraame = cap.read()
    frame = np.flip(fraame, axis=1)
    flagy = 0
    flagr = 0
    flagg = 0
    flagb = 0

    thresholdy = cv2.inRange(frame, yellow_low, yellow_high)
    cv2.line(thresholdy, (180, 0), (180, 600), (255, 255, 255), 1)
    cv2.line(thresholdy, (460, 0), (460, 600), (255, 255, 255), 1)
    cv2.line(thresholdy, (640, 0), (640, 600), (255, 255, 255), 1)
    contours, _ = cv2.findContours(thresholdy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
            cen = cv2.moments(cnt)
            cenx = int(cen["m10"] / cen["m00"])
            ceny = int(cen["m01"] / cen["m00"])
            if cenx in range(0,180):
                print("yel left")
                flagy=1
            elif cenx in range(460,640):
                print("yel right")
                flagy=1
            elif cenx in range(180,460):
                print("yel middle")
                flagy=1
    if flagy==0:
        print("yel not visible")

    thresholdr = cv2.inRange(frame, red_low, red_high)
    cv2.line(thresholdr, (180, 0), (180, 600), (255, 255, 255), 1)
    cv2.line(thresholdr, (460, 0), (460, 600), (255, 255, 255), 1)
    cv2.line(thresholdr, (640, 0), (640, 600), (255, 255, 255), 1)
    contours, _ = cv2.findContours(thresholdr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
            cen = cv2.moments(cnt)
            cenx = int(cen["m10"] / cen["m00"])
            ceny = int(cen["m01"] / cen["m00"])
            if cenx in range(0, 180):
                print("red left")
                flagr = 1
            elif cenx in range(460, 640):
                print("red right")
                flagr = 1
            elif cenx in range(180, 460):
                print("red middle")
                flagr = 1
    if flagr == 0:
        print("red not visible")

    thresholdg = cv2.inRange(frame, green_low, green_high)
    cv2.line(thresholdg, (180, 0), (180, 600), (255, 255, 255), 1)
    cv2.line(thresholdg, (460, 0), (460, 600), (255, 255, 255), 1)
    cv2.line(thresholdg, (640, 0), (640, 600), (255, 255, 255), 1)
    contours, _ = cv2.findContours(thresholdg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
            cen = cv2.moments(cnt)
            cenx = int(cen["m10"] / cen["m00"])
            ceny = int(cen["m01"] / cen["m00"])
            if cenx in range(0, 180):
                print("green left")
                flagg = 1
            elif cenx in range(460, 640):
                print("green right")
                flagg = 1
            elif cenx in range(180, 460):
                print("green middle")
                flagg = 1
    if flagg == 0:
        print("green not visible")
    thresholdb = cv2.inRange(frame, blue_low, blue_high)
    cv2.line(thresholdb, (180, 0), (180, 600), (255, 255, 255), 1)
    cv2.line(thresholdb, (460, 0), (460, 600), (255, 255, 255), 1)
    cv2.line(thresholdb, (640, 0), (640, 600), (255, 255, 255), 1)
    contours, _ = cv2.findContours(thresholdb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
            cen = cv2.moments(cnt)
            cenx = int(cen["m10"] / cen["m00"])
            ceny = int(cen["m01"] / cen["m00"])
            if cenx in range(0, 180):
                print("blue left")
                flagb = 1
            elif cenx in range(460, 640):
                print("blue right")
                flagb = 1
            elif cenx in range(180, 460):
                print("blue middle")
                flagb = 1
    if flagb == 0:
        print("blue not visible")

    cv2.imshow("frame", frame)
    cv2.imshow("thresholdr", thresholdr)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
