import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img.png')

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = np.float32(img)

#cornerHarris(gray-float,square,kernel-size,decimal)
dst = cv2.cornerHarris(img,2,3,0.04)
cv2.imshow('dst',dst)

_,curve = cv2.threshold(img,30,255,cv2.THRESH_BINARY)
cv2.imshow('curve',curve)

cv2.waitKey(0)
cv2.destroyAllWindows()
