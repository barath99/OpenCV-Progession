import cv2
import numpy as np

img = cv2.imread('img.png',1)

pts = np.array([[5,100],[100,100],[25,200]],np.int32)
cv2.polylines(img,[pts],True,(0,0,0),3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
