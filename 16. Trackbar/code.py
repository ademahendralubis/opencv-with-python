#code by codingan

import cv2

def nothing(x):
    pass

#load image
image = cv2.imread('image.png')

#Create Window
cv2.namedWindow('Resizing')

#Create Trackbar
cv2.createTrackbar('width', 'Resizing', 200, 1000, nothing)
cv2.createTrackbar('height', 'Resizing', 200, 1000, nothing)


while True:

    #Get Trackbar Value
    width = cv2.getTrackbarPos('width','Resizing')
    height = cv2.getTrackbarPos('height','Resizing')

    #Resizing image
    resize = cv2.resize(image, (width, height))

    #show original image
    cv2.imshow('resize', resize)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
