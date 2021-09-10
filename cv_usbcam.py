import cv2 as cv
import matplotlib.pyplot as plt


windowName = "Live Video"
cv.namedWindow(windowName)
cap = cv.VideoCapture(0)
print('Width : ' + str(cap.get(3)))
print('Height : ' + str(cap.get(4)))
cap.set(3, 5000)
cap.set(4, 5000)
print('Width : ' + str(cap.get(3)))
print('Height : ' + str(cap.get(4)))
if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False
while ret:
    ret, frame = cap.read()
    cv.imshow(windowName, frame)
    if cv.waitKey(1) == 27:
        break
cv.destroyAllWindows()
cap.release()

