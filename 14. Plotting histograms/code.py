import cv2
import matplotlib.pyplot as plt

#Show image
image = cv2.imread('image.jpg',cv2.IMREAD_GRAYSCALE)

#Show image
cv2.imshow("image", image)

#Show histogram
plt.hist(image.ravel(), 256, [0,256])
plt.show()


cv2.waitKey(0)
