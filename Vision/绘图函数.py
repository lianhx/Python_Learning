import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
