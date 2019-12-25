import cv2
import numpy as np

img = cv2.imread('img.png',1)

#Drawing a circle with cv
cv2.circle(img,(100,63),55,(0,0,0),-3)
#a negative number as last parameter fills the circle

cv2.imshow('window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
