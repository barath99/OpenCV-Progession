import cv2
import numpy as np

img = cv2.imread('img.png',1)

# Drawing a rectangle using cv
cv2.rectangle(img,(260,80),(530,520),(25,25,25),2)
#(img,diagonalA,diagonalB,color,thickness)

cv2.imshow('Window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
