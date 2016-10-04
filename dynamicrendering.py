import numpy as np
import cv2
import time

cap = cv2.VideoCapture("output.avi")
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output2.avi',fourcc, 20.0, (640,480))

fo = open("input.txt","rw+")
lineNumber = 0
line = fo.readline()
framecount = 0
while cap.isOpened():
    ret,frame = cap.read()
    if ret==True:
        startx,starty,endx,endy,threshold = map(int,line.split())
        frame = frame[startx:endx,starty:endy]
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) and 0xFF ==ord('q'):
            break
        framecount = framecount+1
        if framecount%threshold==0:
            line = fo.readline()
    else:
        break

fo.close()
cap.release()
out.release()
cv2.destroyAllWindows()
