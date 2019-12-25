import cv2
import numpy as np

#program to record the video and save it as avi

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
    ret,frame = cap.read()
    out.write(frame)
    cv2.imshow('window',frame)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
