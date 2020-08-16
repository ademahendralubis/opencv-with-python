import cv2

#load image
image = cv2.imread('image.png')

#show image
cv2.imshow('window',image)

while True:
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break;

#save image
cv2.imwrite('a.jpg',image)
