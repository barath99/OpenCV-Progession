import cv2
img=cv2.imread('img.jpg',cv2.IMREAD_COLOR)
# Instead of using cv2.IMREAD_(something) we can use the assigned numbers

# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1
# IMREAD_GRAYSCALE = 0

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
