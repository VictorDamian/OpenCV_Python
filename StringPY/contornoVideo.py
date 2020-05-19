import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while True:
  ret, frame = cap.read()
  if ret==True:
    gray = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
    gauss = cv.GaussianBlur(gray,(5,5),0)
    canny = cv.Canny(gauss,50,150)
    (contornos,_) = cv.findContours(canny.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.imshow('canny', canny)
    if cv.waitKey(1) & 0xFF == ord('s'):
      break
cap.release()
cv.destroyAllWindows()