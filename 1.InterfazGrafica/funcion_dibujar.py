#################################
##--- VictorDamian
##--- Python 3.7.8 - OpenCV 3.5.3
##--- INFO: https://docs.opencv.org/master/dc/da5/tutorial_py_drawing_functions.html
#################################

import numpy as np
import cv2
# Crea imagen base param: (dimensiones)
img = np.zeros((512,512,3), np.uint8)

# dibuja una linea azul de:
# izquierda sup a drecha infe -> [(0,0),(511,511)]
# color -> (255,0,0)
# grosor -> 5
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

# Para dibujar un rectángulo, necesita la esquina superior izquierda y
# la esquina inferior derecha del rectángulo. 
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Para dibujar un círculo, necesita sus coordenadas centrales y su radio
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

# Para dibujar un elipse:
# ubicación del centro (x, y).
# longitud del eje mayor, longitud del eje menor
# startAngle y endAngle denota el inicio y el final del arco de elipse 
# color
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Poligono
# coordenadas de vértices. 
# Convierta esos puntos en una matriz de forma ROWSx1x2 donde ROWS
# son el número de vértices y debe ser de tipo int32. 
# Ejes X y despues Y
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

# agrega texto
font = cv2.FONT_HERSHEY_SIMPLEX
# Coordenadas, fuente, tamaño, color, grosor, tipo de linea
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()