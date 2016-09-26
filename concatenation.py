import cv2
import numpy as np
import sys
import os
import pyaudio  
import wave  
import time

chunk = 1024  
start = 1
Names = sys.argv[1]
Rows = int(sys.argv[2])
Cols = int(sys.argv[3])
Flag = int(sys.argv[4])

NamesList = Names.split(',')

NamesList = np.array(NamesList)
NamesList = np.reshape(NamesList,(Rows,Cols))

f = wave.open(r"audio.wav","rb")  
#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
data = f.readframes(chunk)  


if Rows==2 and Cols==2:
	cap1 = cv2.VideoCapture(NamesList[0][0])
	cap2 = cv2.VideoCapture(NamesList[0][1])
	cap3 = cv2.VideoCapture(NamesList[1][0])
	cap4 = cv2.VideoCapture(NamesList[1][1])
	count = 0
	while cap1.isOpened() or cap2.isOpened() or data!='':
	    ret1,frame1 = cap1.read()
	    ret2,frame2 = cap2.read()
	    ret3,frame3 = cap3.read()
	    ret4,frame4 = cap4.read()
	    both = np.concatenate((frame1,frame2),axis=0)
	    both1 = np.concatenate((frame3,frame4),axis=0)
	    both2 = np.concatenate((both1,both),axis=1)
	    if Flag==1:
	    	both2 = cv2.flip(both2,0)
	    cv2.imshow('Final',both2)
	    stream.write(data)
	    data = f.readframes(chunk)
	    # if start==1:
	    # 	os.system("python playmusic.py")
	    # 	start = 0
	    # stream.write(data)  
    	# data = f.readframes(chunk) 
	    if cv2.waitKey(10) & 0xFF == ord('q'):
	        break
	cap1.release()
	cap2.release()
	cap3.release()
	cap4.release()
	cv2.destroyAllWindows()	
	stream.stop_stream()  
	stream.close()  
	p.terminate()  



if Rows==2 and Cols==1:
	cap1 = cv2.VideoCapture(NamesList[0][0])
	cap3 = cv2.VideoCapture(NamesList[1][0])
	while cap1.isOpened() or cap3.isOpened() or data!='':
	    ret1,frame1 = cap1.read()
	    ret3,frame3 = cap3.read()
	    both = np.concatenate((frame1,frame3),axis=0)
	    if Flag==1:
	    	both = cv2.flip(both,0)
	    cv2.imshow('Final',both)
	    stream.write(data)
	    data = f.readframes(chunk)
	    if cv2.waitKey(10) & 0xFF == ord('q'):
	        break
	cap1.release()
	cap3.release()
	cv2.destroyAllWindows()
	stream.stop_stream()
	stream.close()
	p.terminate()

if Rows==1 and Cols==2:
	cap1 = cv2.VideoCapture(NamesList[0][0])
	cap3 = cv2.VideoCapture(NamesList[0][1])
	while cap1.isOpened() or cap3.isOpened() or data!='':
	    ret1,frame1 = cap1.read()
	    ret3,frame3 = cap3.read()
	    both = np.concatenate((frame1,frame3),axis=1)
	    if Flag==1:
	    	both = cv2.flip(both,0)
	    cv2.imshow('Final',both)
	    stream.write(data)
	    data = f.readframes(chunk)
	    if cv2.waitKey(10) & 0xFF == ord('q'):
	        break
	cap1.release()
	cap3.release()
	cv2.destroyAllWindows()
	stream.stop_stream()
	stream.close()
	p.terminate()

