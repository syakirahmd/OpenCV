import cv2
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    blured_frame = cv.GaussianBlur(frame, (33,33), 0)
    frame_hsv = cv.cvtColor(blured_frame, cv.COLOR_BGR2HSV)
    lower_red = np.array([161, 75, 61])
    higher_red = np.array([179, 255, 250])
    frame_mask = cv.inRange(frame_hsv, lower_red, higher_red)
    # result_frame = cv.bitwise_and(frame, frame, mask=frame_mask)

    contours, _ = cv.findContours(frame_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv.contourArea(contour)
        # print(area)
        if area > 1000:
            cv2.drawContours(frame, contour, -1, (0, 255,0), 2)
    # print(contours)

    cv.imshow("frame", frame)
    cv.imshow("blurred frame", blured_frame)
    # cv.imshow("window", frame_hsv)
    # cv.imshow("Frame Mask", frame_mask)
    # cv.imshow("Result Mask", result_frame)

    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()
