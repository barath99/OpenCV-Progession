import cv2
import numpy as np
import matplotlib.pyplot as plt

img_orig = cv2.imread('img.png')

img = np.copy(img_orig)

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

a=np.array([142,239,229])

mask = cv2.inRange(img,a,a)


bg = cv2.imread('img2.jpg')
bg = bg[0:600,0:800]
bg = cv2.cvtColor(bg,cv2.COLOR_BGR2RGB)

img[mask!=0]=[0,0,0]
bg[mask==0]=[0,0,0]

plt.imshow(img+bg)

plt.show()
