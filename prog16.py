import cv2
import numpy as np

#Using Threshold to perform manipulations

img = cv2.imread('img.png',1)

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img, 30, 255, cv2.THRESH_TOZERO)

#Available modes:
#cv2.THRESH_BINARY
#cv2.THRESH_BINARY_INV
#cv2.THRESH_TRUNC
#cv2.THRESH_TOZERO
#cv2.THRESH_TOZERO_INV

cv2.imshow('Threshold',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
