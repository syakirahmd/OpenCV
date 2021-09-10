import cv2 as cv
import matplotlib.pyplot as plt

windowName = "Live Video"
cv.namedWindow(windowName)
cap = cv.VideoCapture(0)
print('Width : ' + str(cap.get(3)))
print('Height : ' + str(cap.get(4)))
cap = cv.VideoCapture(0)
filename = 'output.avi'
codec = cv.VideoWriter_fourcc('W', 'M', 'V', '2')
framerate = 30
resolution = (640, 480)
Output = cv.VideoWriter(filename, codec, framerate, resolution)
if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False
while ret:
    ret, frame = cap.read()
    Output.write(frame)
    cv.imshow(windowName, frame)
    if cv.waitKey(1) == 27:
        break
cv.destroyAllWindows()
cap.release()
