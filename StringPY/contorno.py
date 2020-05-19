# Convertir la imagen a escala de grises
# Filtrar la imagen para eliminar el ruido
# Aplicar el detector de bordes Canny
# Buscar los contornos dentro de los bordes detectados
# Dibujar dichos contornos

import cv2 as cv

image = cv.imread('IMG/league.jpg')
cv.imshow("1.original", image)

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
gauss = cv.GaussianBlur(gray,(5,5),0)
cv.imshow("2.noise", gauss)

canny = cv.Canny(gauss,50,150)
cv.imshow("3.canny", canny)

(contornos,_) = cv.findContours(canny.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print("He encontrado {} objetos".format(len(contornos)))
cv.drawContours(image,contornos,-1,(0,0,255), 1)

cv.imshow("4.contours", image)
cv.waitKey(0)