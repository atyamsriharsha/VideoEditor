import numpy as np
import os
import cv2
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import shutil
from shutil import copyfile
from cv2 import VideoWriter,imread, resize



os.system("mkdir images")
StartingFrame = 20
EndingFrame = 120
img = np.zeros([100,100,3],dtype=np.uint8)
img.fill(140) # or img[:] = 255
im = Image.fromarray(img)
im.save("images/1.jpg")
img = Image.open("images/1.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-ExtraLight.ttf",16)
draw.text((0,0),"sample",(255,255,255),font=font)
img.save("images/1.jpg")
os.system("avconv -i final.mp4 2>&1 | grep 'Duration' | awk '{print $2}' | sed s/,// > time.txt")
fo = open("time.txt","rw+")
length_of_video = fo.readline()
#print line
os.system("rm time.txt")

cap = cv2.VideoCapture("final.mp4")
count=0
while cap.isOpened():
    if count>StartingFrame and count<EndingFrame:
        copyfile("images/1.jpg","images/frame%d.jpg"%count)
        count = count+1
    else:
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
        vid = VideoWriter('writingtext.avi', fourcc,20, size)
    if size[0] != img.shape[1] and size[1] != img.shape[0]:
        img = resize(img, size)
    vid.write(img)
vid.release()

os.system("rm -r images")
cap.release()
