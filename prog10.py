import cv2
import numpy as np

img = cv2.imread('img.png',1)

#img[a,b] returns the pixel value at (a,b)
px=img[50,100]
print(px)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
