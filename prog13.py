import cv2
import numpy as np

img=cv2.imread('img.png')
img2=cv2.imread('img2.jpg')

img3= img + img2

cv2.imshow('image',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
