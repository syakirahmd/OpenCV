import numpy as np
import cv2 as cv


def empty(z):
    pass


img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('window')
cv.createTrackbar('B', "window", 0, 255, empty)
cv.createTrackbar('G', "window", 0, 255, empty)
cv.createTrackbar('R', "window", 0, 255, empty)
while True:
    cv.imshow('window', img)
    if cv.waitKey(1) == 27:
        break
    blue = cv.getTrackbarPos('B', 'window')
    green = cv.getTrackbarPos('G', 'window')
    red = cv.getTrackbarPos('R', 'window')
    img[:] = [blue, green, red]
cv.destroyWindow('window')
