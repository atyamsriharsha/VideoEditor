import cv2
import os
import sys
from cv2 import VideoWriter,imread, resize

cap = cv2.VideoCapture("final.mp4")
count=0
os.system("mkdir images")
while cap.isOpened():
    ret,frame = cap.read()
    if ret==True:
        cv2.imwrite("images/frame%d.jpg"%count,frame)
        if cv2.waitKey(10)==27:
            break
        count+=1
    else:
        break

fourcc = cv2.cv.CV_FOURCC(*'XVID')
vid = None
count = 867
size = None
for x in xrange(0,count):
    image = "images/frame"+str(count-x-1)+'.jpg'
    if not os.path.exists(image):
        raise FileNotFoundError(image)
    img = imread(image)
    if vid is None:
        if size is None:
            size = img.shape[1], img.shape[0]
        vid = VideoWriter('outvid.avi', fourcc,20, size)
    if size[0] != img.shape[1] and size[1] != img.shape[0]:
        img = resize(img, size)
    vid.write(img)
vid.release()

os.system("rm -r images")
