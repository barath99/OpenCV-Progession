import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    edges = cv2.Canny(frame,20,20)

    cv2.imshow('frame',frame)
    cv2.imshow('edges',edges)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()
cap.release()
