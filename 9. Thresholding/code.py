#code by codingan

import cv2

#load image
image = cv2.imread('image.png')

#Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Convert to Threshold Binary
_, Thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

#Convert to Threshold Binary Inverted
_, Thresh2 = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

#Show Image
cv2.imshow("Gray", gray)
cv2.imshow("Thresh", Thresh)
cv2.imshow("Thresh2", Thresh2)
cv2.waitKey(0)
