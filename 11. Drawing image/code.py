#code by codingan

import cv2

#load image
image = cv2.imread('image.png')

#Drawing image
cv2.rectangle(image, (190,140), (275,218), (0,0,255), -1)
cv2.circle(image, (313,178), 45, (255,0,0),-1)
cv2.line(image, (60,20), (400,200), (0,255,0),5)
cv2.putText(image, "THIS IS TEXT", (500,25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 5)

#Show Image
cv2.imshow("Original", image)
cv2.waitKey(0)
