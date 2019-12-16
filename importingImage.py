import cv2
img=cv2.imread('img.jpg',1)
#img=cv2.imread('img.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
