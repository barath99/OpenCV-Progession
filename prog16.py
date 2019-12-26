import cv2
import numpy as np

#Using Threshold to perform manipulations

cap = cv2.VideoCapture(0)
#img = cv2.imread('img.png',1)
while True:
    rett,img = cap.read()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('Threshold',mask)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
#Available modes:
#cv2.THRESH_BINARY
#cv2.THRESH_BINARY_INV
#cv2.THRESH_TRUNC
#cv2.THRESH_TOZERO
#cv2.THRESH_TOZERO_INV



cv2.destroyAllWindows()
