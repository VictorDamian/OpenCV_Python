#################################
##--- VictorDamian
##--- Python 3.7.8 - OpenCV 3.5.3 - numpy 1.21.1
##--- INFO: https://docs.opencv.org/master/d9/dc8/tutorial_py_trackbar.html
#################################
import cv2
import numpy as np

def nothing(x):
    pass
# Crea ventana
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('Trackbar')
# Trackbars de RGB
cv2.createTrackbar('R','Trackbar',0,255,nothing)
cv2.createTrackbar('G','Trackbar',0,255,nothing)
cv2.createTrackbar('B','Trackbar',0,255,nothing)
switch = '0: OFF \n1 : ON'
cv2.createTrackbar(switch, 'Trackbar' , 0,1, nothing)

while(1):
    cv2.imshow('Trackbar',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
# obtiene posicion de los Tracks
    r = cv2.getTrackbarPos('R','Trackbar')
    g = cv2.getTrackbarPos('G','Trackbar')
    b = cv2.getTrackbarPos('B','Trackbar')
    s = cv2.getTrackbarPos(switch,'Trackbar')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
cv2.destroyAllWindows()

# EJERCICIO:
# Cree una aplicación de pintura con colores ajustables y radio de pincel 
# mediante las barras de seguimiento. Para dibujar, consulte el tutorial 
# anterior sobre el manejo del mouse.