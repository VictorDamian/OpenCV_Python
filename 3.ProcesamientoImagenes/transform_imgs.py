#################################
##--- VictorDamian
##--- Python 3.7.8 - OpenCV 3.5.3
##--- Matplotlib 3.4.2 - numpy 1.21.1
##--- URL: https://docs.opencv.org/master/da/d6e/tutorial_py_geometric_transformations.html
#################################
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

path_image = 'img/ellen3.png'
path_sudoku = 'img/sudoku.png'

# cambiar el tamaño de la imagen
def scaling(image):
    img = cv.imread(image)
    print('Tamaño actual: ', image.shape)
    # metodo 1
    res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
    # metodo 2
    height, width = img.shape[:2]
    res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_LINEAR)
    # metodo 3 - sin distorcion
    window_height = 300
    aspect_ratio = float(image.shape[1])/float(image.shape[0])
    window_width = window_height/aspect_ratio
    image = cv.resize(image, (int(window_height),int(window_width)))
    
    print('Tamaño redimensionado: ', image.shape)
    cv.imshow("Ventana", res)
    cv.waitKey(0)
    cv.destroyAllWindows()

def traslation(image):    
    img = cv.imread (image, 0)
    filas, columnas = img.shape
    # Angulo de inclinacion 
    # cambio de direccion
    # [,,x],[,,y]
    M = np.float32 ([[1,0,100],
                     [0,1,50]])
    dst = cv.warpAffine (img, M, (columnas, filas))
    cv.imshow ('img' , dst)
    cv.waitKey (0)
    cv.destroyAllWindows ()

def rotation(image):
    img = cv.imread(image,0)
    rows,cols = img.shape
    # cols-1 y rows-1 son los límites de coordenadas.
    # ejem: (ancho//2,alto//2),15,1
    M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
    dst = cv.warpAffine(img,M,(cols,rows))
    cv.imshow ('img' , dst)
    cv.waitKey (0)
    cv.destroyAllWindows ()

# Matriz 2x3
def transformation(image):
    img = cv.imread(image)
    rows,cols,ch = img.shape
    # [x,y]
    pt1 = [50,50]
    pt2 = [200,50]
    pt3 = [50,200]
    # ubicacion
    pts1 = np.float32([pt1,pt2,pt3])
    # traslacion
    pts2 = np.float32([[10,100],[200,50],[100,250]])

    cv.circle(img,(pt1),5,(255,0,0),-1)
    cv.circle(img,(pt2),5,(255,0,0),-1)
    cv.circle(img,(pt3),5,(255,0,0),-1)

    M = cv.getAffineTransform(pts1,pts2)
    dst = cv.warpAffine(img,M,(cols,rows))
    plt.subplot(121),plt.imshow(img),plt.title('Entrada')
    plt.subplot(122),plt.imshow(dst),plt.title('Salida')
    plt.show()

# Matriz 3x3
def perspective(image):
    img = cv.imread(image)
    rows,cols,ch = img.shape
    pt1 = [56,65]
    pt2 = [384,57]
    pt3 = [29,397]
    pt4 = [407,401]
    # 4 puntos en la imagen de entrada 
    pts1 = np.float32([pt1,pt2,pt3,pt4])
    # puntos correspondientes en la imagen de salida
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    # conoce a sus propiedades
    print(img.shape)
    # linea hori
    cv.line(img,(0,219),(439,219),(0,255,0),2)
    # linea vert
    cv.line(img,(219,0),(219,439),(0,255,0),2)
    
    cv.circle(img,(pt1),5,(255,0,0),-1)
    cv.circle(img,(pt2),5,(255,0,0),-1)
    cv.circle(img,(pt3),5,(255,0,0),-1)
    cv.circle(img,(pt4),5,(255,0,0),-1)
    # encontrar matriz de transformacion
    M = cv.getPerspectiveTransform(pts1,pts2)
    # aplica perspectiva
    dst = cv.warpPerspective(img,M,(300,300))
    
    plt.subplot(121),plt.imshow(img),plt.title('Input')
    plt.subplot(122),plt.imshow(dst),plt.title('Output')
    plt.show()

#perspective(path_sudoku)
#transformation(path_image)    
#rotation(path_image)
#scaling(path_image)
#traslation(path_image)
#rotateImg(path_image)
#rotateWithMat(path_image)