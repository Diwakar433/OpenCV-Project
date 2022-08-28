import cv2
import numpy as np

img = cv2.imread("Resouces/girl.jpg")
print(img.shape)



imgResizes = cv2.resize(img,(700,1000))

imgCropped = img[0:200,300:500]

cv2.imshow("Image", img)
cv2.imshow("Image resize",imgResizes)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)