import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurred_frame = cv.GaussianBlur(gray_frame, (5,5), 0)
    laplacian_frame = cv.Laplacian(blurred_frame, cv.CV_64F)
    canny_frame = cv.Canny(blurred_frame, 25, 75)
    cv.imshow("Gray Video", gray_frame)
    cv.imshow("Blurred Gray Video", blurred_frame)
    cv.imshow("Laplacian Video", laplacian_frame)
    cv.imshow("canny Video", canny_frame)
    if cv.waitKey(1) == 27:
        break
cap.release()
cv.destroyAllWindows()
