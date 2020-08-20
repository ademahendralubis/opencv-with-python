#code by codingan

import cv2

#load image
image = cv2.imread('image.png')

#load the video
# video = cv2.VideoCapture('video.mp4')

# # Load the camera device
# camera = cv2.VideoCapture(0)



#converting to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#show image
cv2.imshow('window',gray)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()


#show video
# while video.isOpened():
#     #capture frame by frame
#     _, frame = video.read()
#     converting to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     #show the frame
#     cv2.imshow('video',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# video.release()
# cv2.destroyAllWindows()

#Show image from the camera
# while True:
#     ret, frame = camera.read()
#
#     #converting to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('camera 1', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When all done, release the capture and close all opened windows
# camera.release()
# cv2.destroyAllWindows()
