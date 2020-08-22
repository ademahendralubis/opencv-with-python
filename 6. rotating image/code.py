#code by codingan

import cv2

#load image
image = cv2.imread('image.png')
print(image.shape)

#extract the height and width of the image
h, w, _ = image.shape

#center of the image
center = (w/2, h/2)

#set rotation (center coordinate, angles, scale)
rotation = cv2.getRotationMatrix2D(center, -10, -0.1)

#rotate image (source, rotation setting, (width, height))
rotated_img = cv2.warpAffine(image, rotation, (w,h))

#show image
cv2.imshow("rotated img", rotated_img)
cv2.waitKey(0)
