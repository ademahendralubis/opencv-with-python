#code by codingan

import cv2

#load image
image = cv2.imread('image.png')

print(image.shape)

resize = cv2.resize(image, (200,200))

cv2.imshow('original', image)
cv2.imshow('resized', resize)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

cv2.imwrite("resize.png",resize)
