import cv2
import numpy as np
import matplotlib.pyplot as plt

#openCV reads in image as BGR but the most used form is RGB
#matplotlib prints in RGB format.

img = cv2.imread('img.png')

#plt.imshow(img)
#The image is inverted form of R and B

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
