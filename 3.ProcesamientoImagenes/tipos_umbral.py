#################################
##--- VictorDamian
##--- Python 3.7.8 - OpenCV 3.5.3 
##--- Matplotlib 3.4.2
##--- INFO: https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html
#################################

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

def umbralSimple():
    img = cv.imread('img/ellen3.png',0)
    # argumentos: (img, umbral, valor maximo de umbral)
    # tipos de umbrales
    ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
    ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
    ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
    ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
    for i in range(6):
        # trazar varias imgs
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()

# umbral para diferentes regiones de la imagen
def umbralAdaptativo():
    img = cv.imread('img/sudoku.png',0)
    img = cv.medianBlur(img,5)
    # umbral global
    ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

    th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                cv.THRESH_BINARY,11,2)
    th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv.THRESH_BINARY,11,2)
    titles = ['Original Image', 'Global Thresholding (v = 127)',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']

    # azar todas las imágenes y sus histogramas
    images = [img, th1,
              th2, th3]
    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()    

# Filtro para ruido
def binaryOysu():
    img = cv.imread('img/noisy.png',0)
    # umbral global
    ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    # El umbral de Otsu
    ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    #  Umbral de Otsu después del filtrado gaussiano
    blur = cv.GaussianBlur(img,(5,5),0)
    ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    # azar todas las imágenes y sus histogramas
    images = [img, 0, th1,
            img, 0, th2,
            blur, 0, th3]
    titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
            'Original Noisy Image','Histogram',"Otsu's Thresholding",
            'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
    for i in range(3):
        plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
        plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])

        plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
        plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
        
        plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
        plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
    plt.show()

#umbralAdaptativo()
#binaryOysu()