import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv2.imshow('cam',frame)
    cam2gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret1, mask = cv2.threshold(cam2gray,100,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('processed',mask)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cap.release()
cv2.destroyAllWindows()
