#code by codingan

import cv2

#load image
image = cv2.imread('image.jpg')

#Resize image
image = cv2.resize(image, (500,500))

#Average Blur
averageBlur = cv2.blur(image,(10,10))

#Gaussian Blur
gaussianBlur = cv2.GaussianBlur(image, (5, 5), 0)

#Median Blur
median = cv2.medianBlur(image,5)

#Bilateral Filter
bilateral = cv2.bilateralFilter(image,9,75,75)

#Show Image
cv2.imshow("Original", image)
cv2.imshow("averageBlur", averageBlur)
cv2.imshow("gaussianBlur", gaussianBlur)
cv2.imshow("median", median)
cv2.imshow("bilateral", bilateral)
cv2.waitKey(0)
