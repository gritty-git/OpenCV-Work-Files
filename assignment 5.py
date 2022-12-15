import cv2
import numpy as np
cap = cv2.VideoCapture(0)
yellow_low = np.array([0, 127, 127])
yellow_high = np.array([127, 255, 255])

while True:
	_, frame = cap.read()
	

	threshold = cv2.inRange(frame, yellow_low, yellow_high)
	cv2.imshow("threshold", threshold)

	contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
		approx = cv2.approxPolyDP(cnt, 0.0125 * cv2.arcLength(cnt, True), True)

		if len(approx) > 3:

			mask = cv2.fillPoly(threshold, [approx], (0, 0, 0))
			res = cv2.bitwise_and(frame, frame, mask=mask)
			cv2.imshow("res", res)

	key = cv2.waitKey(1)
	if key == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()


