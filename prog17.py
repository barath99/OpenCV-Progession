import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    ret1, threshed = cv2.threshold(frame,12,255,cv2.THRESH_BINARY)
    cv2.imshow('Original',frame)
    cv2.imshow('Threshold set',threshed)

    grayscaled = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret21, threshed2 = cv2.threshold(grayscaled,12,255,cv2.THRESH_OTSU)
    cv2.imshow('gray',grayscaled)
    cv2.imshow('gray2',threshed2)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cap.release()
cv2.destroyAllWindows()
