import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    _,frame = cap.read()
    cv2.imshow('Original',frame)

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray',frame)

    a = cv2.threshold(frame,100,255,cv2.THRESH_BINARY_INV)

    retval,contours,hierarchy = cv2.findContours(a,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    all_contours = cv2.drawContours(frame,contours, -1, (0,255,0),2)

    cv2.imshow('contours',all_contours)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cap.release()
cv2.destroyAllWindows()
