import cv2


thresh = 45
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if cv2.waitKey(1) == ord('p'):
        thresh += 10
    ret1, output = cv2.threshold(frame, thresh, 255, cv2.THRESH_BINARY)
    print(thresh)
    cv2.imshow('Thresholding App', output)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()