import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    img_range = cv.inRange(hsv, np.array([40, 50, 50]), np.array([80, 255, 255]))
    # img_range dalam bentuk masking atau disebut binary image
    output = cv.bitwise_and(frame, frame, mask=img_range)
    cv.imshow("original", output)
    cv.imshow("output", frame)
    cv.imshow("image mask", img_range)
    if cv.waitKey(1) == 27:
        break
cv.destroyAllWindows()
cap.release()
