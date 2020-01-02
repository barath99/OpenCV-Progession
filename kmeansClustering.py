import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('img2.jpg')

pixel_vals = img.reshape((-1,3))
pixel_vals = np.float32(pixel_vals)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

k=2

retval, labels, centers = cv2.kmeans(pixel_vals,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers)
segmented_data = centers[labels.flatten()]

segmented_image = segmented_data.reshape((img.shape))
labels_reshape = labels.reshape(img.shape[0],img.shape[1])

cv2.imshow('',segmented_image)

