#################################
##--- VictorDamian
##--- Python 3.7.8 - OpenCV 3.5.3
##--- Matplotlib 3.4.2 - numpy 1.21.1
##--- INFO: https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html
#################################
import numpy as np
import cv2 as cv
import random
from matplotlib import pyplot as plt

def noisy(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    filas = image.shape[0]
    colum = image.shape[1]
    for i in range(filas):
        for j in range(colum):
            rdm = random.random()
            if rdm < prob:
                output[i][j] = 0
            elif rdm > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

img = cv.imread('img/sudoku.png')
kernel = np.ones((5,5),np.float32)/25
# convolucion2D ayuda a eliminar ruido
dst = cv.filter2D(img,-1,kernel)
# 
blur = cv.blur(img,(5,5))
# elimina el ruido gaussiano
blurG = cv.GaussianBlur(img,(5,5),0)
# efectivo para ruido pimienta, sal
pm = noisy(img, 0.20) # aplica ruido
median = cv.medianBlur(pm,5)
# eliminación de ruido y mantiene los bordes nítidos. (lento)
blurB = cv.bilateralFilter(img,9,75,75)

title = ['Original','Averaging','Blur','BlurG','MedianB','BlurB']
images=[img,dst,blur,blurG,median,blurB]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])
plt.show()