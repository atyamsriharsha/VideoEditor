import numpy as np
import cv2

cap = cv2.VideoCapture('output.avi')

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc = cv2.cv.CV_FOURCC(*'XVID')
# # av_dict_set(&This->opts, "tune", "zerolatency", 0)
# # avcodec_open2(This->context, This->codec, &This->opts)
# fourcc = cv2.cv.CV_FOURCC(*'X264')

out = cv2.VideoWriter('output2.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        #cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
