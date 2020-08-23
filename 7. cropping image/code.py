#code by codingan

import cv2

#load image
image = cv2.imread('image.png')
print(image.shape)

crop = image[130:230, 200:270]

cv2.imshow("full", image)
cv2.imshow('crop',crop)
cv2.waitKey(0)
