import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# VideoCapture takes the id of camera that is connected to the pc.
# 0 denotes the first camera

while True:
    ret, frame = cap.read()
    # cap.read() function returns (ret value-Success/Failure,image)

    cv2.imshow('Window',frame)
    #imshow function parameters are (windows name, image)

    if cv2.waitKey(8) & 0b1111111 == ord('x'):
        #waitkey has delay (in ms) as parameter
        #8 LSB doesnt change when numlock is On or Off even when x is pressed
        #hence we do a bitwise and to remove the other bits from being checked
        break

cap.release()
#cap.release function releases the capturing function.(stops capturing)
cv2.destroyAllWindows()
