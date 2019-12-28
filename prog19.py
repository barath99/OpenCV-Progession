import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#blurring

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    blur = cv2.GaussianBlur(frame,(101,101),0)


    kernel = np.ones((15,15),np.float32)/225
    blur = cv2.filter2D(blur, -1,kernel)

    ret, thresh = cv2.threshold(frame,20,255,cv2.THRESH_BINARY)

    cv2.imshow('frame',frame)
    cv2.imshow('smoothed',blur)
    cv2.imshow('thresh',thresh)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()

    

    
