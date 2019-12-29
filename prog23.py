import cv2
import numpy as np

img = cv2.imread('img.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,100,0.01,10)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),2,255,-1)
cv2.imshow('Corner',img)
