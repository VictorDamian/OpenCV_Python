#################################
##--- VictorDamian
##--- Python 3.7.8 - OpenCV 3.5.3 - imutils 0.5.4
##--- INFO: https://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html
#################################

import cv2 as cv
import imutils

path_img = 'img/ellen2.jpg'
img = cv.imread(path_img)

def propiedadesImg(img):
    # acceder a un valor de píxel por sus coordenadas de fila y columna.
    px = img[100,100]
    print(px)
    # accediendo solo al píxel azul
    azul = img[100,100,0]
    print(azul)
    # modificar los valores de los pixeles
    img [100,100] = [255,255,255]
    print(img[100,100])
    # Mejor método de edición y acceso a píxeles:
    img.itemset ((10,10,2),100)
    img.item (10,10,2)
    # Accede a las propiedades
    # (Filas, columnas, canales)
    print(img.shape)
    # Accede al número total de píxeles
    print(img.size)
    # El tipo de datos de la imagen 
    print(img.dtype)
    img = imutils.resize(img,height=600)
    # dividir la imagen BGR en canales individuales.
    b, g, r = cv.split(img)
    img=cv.merge((b,g,r))

