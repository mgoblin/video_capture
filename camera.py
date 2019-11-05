import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('cars.mp4')

ret, frame = cap.read()
# cv2.imshow('frame', frame)

plt.subplot(1, 1, 1)
plt.imshow(frame)
plt.show()

while 1:
    ret, frame = cap.read()

    if frame is not None:
        cv2.imshow('frame', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
