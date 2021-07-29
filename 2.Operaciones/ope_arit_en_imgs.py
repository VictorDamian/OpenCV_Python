  
#################################
##--- VictorDamian
##--- Python 3.7.8 - OpenCV 3.5.3 - Numpy 1.21.1
##--- INFO: https://docs.opencv.org/master/d0/d86/tutorial_py_image_arithmetics.html
#################################
import cv2
import numpy as np

# Adición de imágenes
x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x,y))
print(x+y)

# Mezcla de imágenes
img1 = cv2.imread ( 'img/ellen3.png' )
img2 = cv2.imread ( '/img/ellen33.png')
dst = cv2.addWeighted (img1,0.7, img2,0.6,0)
cv2.imshow ( 'dst' , dst)
cv2.waitKey (0)
cv2.destroyAllWindows ()

def operacionesBit():
    # img1: Fondo, img2: Logo
    img1 = cv2.imread('img/figura.jpg')
    img2 = cv2.imread('img/ellen3.png')

    # Crea ROI, ubicado en la parte izquierda superior
    rows,cols,channels = img2.shape
    roi = img1[0:rows, 0:cols ]

    # crea una mascara para el logo
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    # Mascara inversa para el logo
    mask_inv = cv2.bitwise_not(mask)
    # oscurezca el área del logotipo en el ROI
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

    # captura solo la region del logo
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

    # Agrega el logo en el ROI
    dst = cv2.add(img1_bg,img2_fg)
    img1[0:rows, 0:cols ] = dst

    cv2.imshow('Ventana',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ejercicios
# Cree una presentación de diapositivas de imágenes en una carpeta 
# con una transición suave entre imágenes utilizando la función cv.addWeighted