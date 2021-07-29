#################################
##--- VictorDamian
##--- Python 3.7.8 - OpenCV 3.5.3
##--- INFO: https://docs.opencv.org/master/db/deb/tutorial_display_image.html
#################################
import cv2 as cv
import sys

path_img = 'img/ellen2.jpg'

def openFile(image):
    img  = cv.imread(cv.samples.findFile(image))
    # Muestra una ventana si se carga correctamente
    if img is None:
        sys.exit('No se pudo leer la imagen')
    cv.imshow("Vista", img)
    k = cv.waitKey(0)
    # Si presiona s se guarda en un archivo
    if k == ord('s'):
        cv.imwrite('folder/ejemplo.png', img)
    cv.destroyAllWindows()

image = openFile(image=path_img)