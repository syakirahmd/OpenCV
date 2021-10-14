import cv2 as cv
import numpy as np

cap = cv.VideoCapture(r'C:\Users\syakir\Downloads\object_tracking\highway.mp4')
object_detector = cv.createBackgroundSubtractorMOG2(history=100, varThreshold=50)


while True:
    _, frame = cap.read()
    roi = frame[340: 720, 500: 800]
    mask = object_detector.apply(roi)
    _, mask = cv.threshold(mask, 254, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 100:
            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cv.drawContours(roi, cnt, -1, (0, 255, 0), 2)

    cv.imshow('Original Video', frame)
    cv.imshow('Masked', mask)
    if cv.waitKey(30) == 27:
        break
cap.release()
cv.destroyAllWindows()