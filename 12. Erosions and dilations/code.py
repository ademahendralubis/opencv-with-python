#code by codingan

import cv2
import numpy as np

#load image
image = cv2.imread('image.png')

#Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Convert to Threshold Binary Inverted
_, Thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

#Erosions
erode = cv2.erode(Thresh, None, iterations=5)

#Dilations
dilate = cv2.dilate(Thresh, None, iterations=5)

#Show Image
cv2.imshow("Thresh", Thresh)
cv2.imshow("erode", erode)
cv2.imshow("dilate", dilate)
cv2.waitKey(0)
