import cv2
import numpy as np

img = cv2.imread('img.png',1)

#writing on the screen
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'BARATH',(70,150),font,6,(255,255,255),5,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
