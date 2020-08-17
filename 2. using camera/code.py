# code by codingan

import cv2

# Load the camera device
camera = cv2.VideoCapture(0)

# Show image from the camera
while True:
    ret, frame = camera.read()

    cv2.imshow('camera 1', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When all done, release the capture and close all opened windows
camera.release()
cv2.destroyAllWindows()
