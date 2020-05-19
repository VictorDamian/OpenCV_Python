import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('IMG/balon.jpg')
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()