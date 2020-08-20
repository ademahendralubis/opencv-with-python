#code by codingan

import cv2

#load image
image = cv2.imread('image.png')

#print the shape of image
print(image.shape)

#resizing image (width,height)
resize = cv2.resize(image, (200,200))

#show original image
cv2.imshow('original', image)

#show resized image
cv2.imshow('resized', resize)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

#save the resized image
cv2.imwrite("resized.png",resize)
