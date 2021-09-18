import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\syakir\Pictures\Camera Roll\test1.jpg', cv.IMREAD_GRAYSCALE)  # coovert img ke gray scale
img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
img = cv.flip(img, 1)
template = img[180:360, 80:250]  # 180:360 = tinggi | 80:250 = lebar
# print(img.shape)

### find template result
result = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)

### Show Image
cv.imshow('test', img)
cv.imshow('templete', template)
cv.imshow('result', result)
cv.waitKey(0)
cv.destroyAllWindows()
