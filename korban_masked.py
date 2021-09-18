import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def empty(z):
    pass


cv.namedWindow('trackbar')
# img = cv.imread(r'C:\Users\syakir\Downloads\korban.jpg')
# img = cv.resize(img, (520, 495))
cap = cv.VideoCapture(0)
# img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.createTrackbar('Hue max', 'trackbar', 179, 179, empty)
cv.createTrackbar('Hue min', 'trackbar', 161, 179, empty)
cv.createTrackbar('Saturation max', 'trackbar', 255, 255, empty)
cv.createTrackbar('Saturation min', 'trackbar', 75, 255, empty)
cv.createTrackbar('Value max', 'trackbar', 250, 255, empty)
cv.createTrackbar('Value min', 'trackbar', 61, 255, empty)

# titles = ['oriiginal', 'hsv original']
# images = [img, img_hsv]
while True:
    _, frame = cap.read()
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    Hue_max = cv.getTrackbarPos('Hue max', 'trackbar')
    Hue_min = cv.getTrackbarPos('Hue min', 'trackbar')
    Sat_max = cv.getTrackbarPos('Saturation max', 'trackbar')
    Sat_min = cv.getTrackbarPos('Saturation min', 'trackbar')
    Val_max = cv.getTrackbarPos('Value max', 'trackbar')
    Val_min = cv.getTrackbarPos('Value min', 'trackbar')

    upper = np.array([Hue_max, Sat_max, Val_max])
    lower = np.array([Hue_min, Sat_min, Val_min])
    mask = cv.inRange(frame_hsv, lower, upper)

    img_result = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("original Video", frame)
    cv.imshow("HSV Video", frame_hsv)
    cv.imshow(" Masked Video", mask)
    cv.imshow("Video result", img_result)
    # allimage = cv.hconcat([img, img_hsv, img_result])
    # cv.imshow("result", allimage)

    if cv.waitKey(3) == 27:
        break
cap.release()
cv.destroyAllWindows()
