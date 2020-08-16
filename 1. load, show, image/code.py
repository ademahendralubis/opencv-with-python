import cv2

image = cv2.imread('image.png')

cv2.imshow('window',image)

while True:
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break;

cv2.imwrite('a.jpg',image)
