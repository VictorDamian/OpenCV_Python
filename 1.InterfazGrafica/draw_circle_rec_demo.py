#################################
##--- VictorDamian
##--- Python 3.7.8 - OpenCV 3.5.3 - Numpy 1.21.1
##--- INFO: https://docs.opencv.org/master/db/d5b/tutorial_py_mouse_handling.html
#################################
import cv2
import numpy as np

def draw_circle1(event,x,y,flags,param):
    img = np.zeros((512,512,3), np.uint8)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),50,(0,255,0),-1)
        cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle1)
    while(1):
        cv2.imshow('image',img)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

drawing = False # si se presiona el mause es true
mode = True # modo rec o circ
ix,iy = 1,1
# función de devolución de llamada del mouse
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    # mientras de clic
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
    # un solo clic
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
# alternar entre rectángulo y círculo.
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()