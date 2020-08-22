#code by codingan

import cv2

#load image
image = cv2.imread('image.png')
print(image.shape)
h, w, _ = image.shape

center = (w/2, h/2)
rotation = cv2.getRotationMatrix2D(center, -10, -0.1)
rotated_img = cv2.warpAffine(image, rotation, (w,h))
cv2.imshow("rotated img", rotated_img)
cv2.waitKey(0)
