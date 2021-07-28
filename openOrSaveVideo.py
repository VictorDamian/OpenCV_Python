#################################
##--- VictorDamian
##--- Python 3.7.8 - OpenCV 3.5.3
##--- INFO: https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
#################################
import cv2 as cv

path_video = 'img/videoEntrada.mp4'
cam = 0

def saveVideo(camera):
    cap = cv.VideoCapture(camera)
    # Codec del video
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    # (nombre,codec,fps,tamaño)
    out = cv.VideoWriter('salida.avi', fourcc, 20.0, (640,  480))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error frame...")
            break
        # Voltea el frame
        frame = cv.flip(frame, 0)
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('s'):
            break
    # Libera recursos
    cap.release()
    out.release()
    cv.destroyAllWindows()

def openVideoOrCam(video):
    cap = cv.VideoCapture(video if video else 0)
    if not cap.isOpened():
        print("No se puede abrir la camara")
    while True:
        # captura cada frame
        success, frame = cap.read()
        if not success:
            print("Error frame.")
            break
        # si es correcto aqui ejecuta operaciones
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # muestra el frame
        cv.imshow('Video', gray)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    # termina la captura
    cap.release()
    cv.destroyAllWindows()

# parametro 'cam' para abrir la camara
openVideoOrCam(path_video)

saveVideo(cam)