import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    laplacian = cv2.Laplacian(frame2,cv2.CV_64F)

    cv2.imshow('original',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('frame2',frame2)
    
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cap.release()
cv2.destroyAllWindows()

