#################################
##--- VictorDamian
##--- Python 3.7.8 - OpenCV 3.5.3 
##--- Numpy 1.21.1 - imutils 0.5.4
##--- URL: https://docs.opencv.org/master/df/d9d/tutorial_py_colorspaces.html
#################################
# Cambio de espacio de color
import cv2
import numpy as np
import imutils

path_video='img/test_p.mp4'

def ArrayImgs(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def openVideoOrCam(video):
    cap = cv2.VideoCapture(video if video else 0)
    if not cap.isOpened():
        print("No se pudo abrir la camara")
    while True:
        success, frame = cap.read()
        if not success:
            print("Error frame.")
            break
        
        frame = imutils.resize(frame, width=640)
        # Convertir de espacio de color BGR a HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # definir el rango de color azul en HSV
        # [tono,saturacion,valor]
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        # Umbral de la imagen HSV para obtener solo colores azules
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # mascara bit a bit
        res = cv2.bitwise_and(frame,frame, mask= mask)
        stk = ArrayImgs(0.8,([frame, mask],[frame, res],))
        
        cv2.imshow("Window", stk)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

openVideoOrCam(path_video)

# Encontrar los valores HSV
verde = np.uint8 ([[[0,255,0]]])
hsv_verder = cv2.cvtColor(verde, cv2.COLOR_BGR2HSV)
print(hsv_verder)

# Ejercicios :
# Intente encontrar una manera de extraer más de un objeto de color, por ejemplo, extraiga objetos rojos, azules y verdes simultáneamente.