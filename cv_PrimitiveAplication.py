import cv2 as cv
import numpy as np

img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('window')


def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 40, (0, 255, 0), -1)
    if event == cv.EVENT_MBUTTONDOWN:
        cv.circle(img, (x, y), 20, (0, 0, 255), -1)
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 30, (255, 0, 0), -1)


cv.setMouseCallback('window', draw_circle)
while True:
    cv.imshow('window', img)
    if cv.waitKey(20) == 27:
        break
cv.destroyAllWindows()