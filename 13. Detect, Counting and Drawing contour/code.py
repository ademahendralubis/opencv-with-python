#code by codingan

import cv2

#load image
image = cv2.imread('image.png')

#Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Convert to Threshold Binary
_, Thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

#Find all Countours
contours, _ = cv2.findContours(Thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Put text
cv2.putText(image, "Number of contours = {}".format(len(contours)), (400,35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

#Drawing the contours
cv2.drawContours(image, contours, -1, (0,0,255),3)

#Show image
cv2.imshow("image", image)
cv2.waitKey(0)
