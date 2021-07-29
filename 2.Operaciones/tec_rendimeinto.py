#################################
##--- VictorDamian
##--- Python 3.7.8 - OpenCV 3.5.3
##--- INFO: https://docs.opencv.org/master/dc/d71/tutorial_py_optimization.html
#################################
import cv2 as cv

img1 = cv.imread('img/ellen3.jpg')
# devuelve el número de ciclos de reloj después de un evento
e1 = cv.getTickCount()
# filtrado de la mediana con núcleos de tamaños impares que van de 5 a 49. 
for i in range(1,49,2):
    img1 = cv.medianBlur(img1,i)
# devuelve la frecuencia de los ciclos de reloj o el número de
# ciclos de reloj por segundo.
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print(t)