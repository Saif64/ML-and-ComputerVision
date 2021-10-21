# python script to open img in openCV
import cv2

img = cv2.imread('../DATA/00-puppy.jpg')

while True:
    cv2.imshow('puppy', img)

    # if we wait at least 1ms AND we have pressed the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
