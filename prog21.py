import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame,0)
    sobelx = cv2.Sobel(frame,0,1,0,ksize=5)
    sobely = cv2.Sobel(frame,0,0,1,ksize=5)

    cv2.imshow('original',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cap.release()
cv2.destroyAllWindows()

