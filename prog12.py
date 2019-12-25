import cv2
import numpy as np

img = cv2.imread('img.png',1)

imgPortion = img[80:520,260:530]
#IMPORTANT NOTE: parameters (y:y+h,x:x+w)
img[0:440,0:270]=imgPortion

cv2.imshow('Window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
