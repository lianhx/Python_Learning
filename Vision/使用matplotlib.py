import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Vision/src/messi5.jpg', 0)
plt.imshow(img, 'gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
