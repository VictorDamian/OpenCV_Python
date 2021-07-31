#################################
##--- VictorDamian
##--- Python 3.7.8 - OpenCV 3.5.3
##--- Matplotlib 3.4.2 - numpy 1.21.1
##--- INFO: https://docs.opencv.org/master/d9/d61/tutorial_py_morphological_ops.html
#################################

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('img/j.png', 0)

kernel = np.ones((5,5),np.uint8)
# param: (img, kernel, )
# eliminar pequeños ruidos
erosion = cv.erode(img,kernel,iterations = 1)
# aumenta la region
dilation = cv.dilate(img,kernel,iterations = 1)
# aplca ruido
# para redicir ruido
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
# para cerrar agujeros del centro del objeto
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
# para el contorno del obj
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

titles = ['Normal','erosion', 'dilation','opening',
          'closing','gradient','tophat','blackhat']

# azar todas las imágenes y sus histogramas
images = [img,erosion,dilation,opening, 
          closing,gradient,tophat,blackhat]

# Rectangular Kernel
print(cv.getStructuringElement(cv.MORPH_RECT,(5,5)))
# Elliptical Kernel
print(cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5)))
# Cross-shaped Kernel
print(cv.getStructuringElement(cv.MORPH_CROSS,(5,5)))

for i in range(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()  