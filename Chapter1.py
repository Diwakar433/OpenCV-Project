import cv2
from cv2.cv2 import VideoCapture

print("pakage install")

# read and show the image
# img = cv2.imread("Resouces/girl.jpg")
# cv2.imshow("Output", img)
# cv2.waitKey(0)


# capture the image and show per frame
# cap =cv2.VideoCapture("Resouces/4k.mp4")

# while True:
#    success, img = cap.read()
#    cv2.imshow("Video", img)
#    if cv2.waitKey(1) & 0xF == ord('q'):
#       break

# open webcamra

cap: VideoCapture = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xF == ord('q'):
        break
