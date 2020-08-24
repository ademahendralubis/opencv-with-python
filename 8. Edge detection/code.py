#code by codingan

import cv2

#load image
image = cv2.imread('image2.jpg')

#convert to canny
canny1 = cv2.Canny(image, 50, 100)
canny2 = cv2.Canny(image, 150, 180)
canny3 = cv2.Canny(image, 200, 230)

#show image
cv2.imshow("original image",image)
cv2.imshow("canny1",canny1)
cv2.imshow("canny2",canny2)
cv2.imshow("canny3",canny3)
cv2.waitKey(0)
