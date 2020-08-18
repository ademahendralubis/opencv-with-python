# code by codingan


import cv2

#load the video
video = cv2.VideoCapture('video.mp4')

#set video codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#set Video Writer and define the output filename
out = cv2.VideoWriter('output.avi',fourcc, 60.0, (1920,1080))

while video.isOpened():
    #capture frame by frame
    _, frame = video.read()

    #write the frame into output file
    out.write(frame)

    #show the frame
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#to release videoCapture and videoWriter, when everything is done
video.release()
out.release()

#close all windows
cv2.destroyAllWindows()
