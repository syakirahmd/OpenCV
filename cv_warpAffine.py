import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\syakir\Downloads\cat.jpg', 1)
img = cv2.resize(img, None, fx=0.55, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.rectangle(img, (100, 100), (200,200), (0,0,255), 2)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow("cat", 255 - img)
cv2.imshow("cat", img)
cv2.waitKey(0)
cv2.destroyAllWindows()