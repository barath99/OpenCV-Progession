import cv2
import numpy as np

# Drawing lines over image using CV

img = cv2.imread('img.png',0)

cv2.line(img,(0,0),(150,150),(255,255,255),1)
#RGB -> (b,g,r) Everything is from 0 to 255

cv2.imshow('Window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
