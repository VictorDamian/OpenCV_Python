import cv2 as cv
import numpy as np
#from matplotlib import pyplot as plt

img = cv.imread('IMG/balon.jpg')
font = cv.FONT_HERSHEY_COMPLEX
text=cv.putText(img,"hola",(15,30),font,1,(0,0,0),2,cv.LINE_AA)
fromCenter = False
roi = cv.selectROI(img,fromCenter)
imCrop = img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
bola = img [280: 340, 330: 390]
cv.imshow("Imagen",imCrop)
print(bola)
cv.waitKey()
cv.destroyAllWindows()