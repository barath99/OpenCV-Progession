import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret1, frame1 = cap.read()
    cv2.imshow('Window1',frame1)

    #converting color stream to grayscale cvtColor Function is used.
    gframe = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Window2',gframe)

    if cv2.waitKey(1) & 0b1111111 == ord('x'): 
       break        
    
cap.release()
cv2.destroyAllWindows()    
