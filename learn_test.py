import cv2


img = cv2.imread('1-3.jpg')
img = cv2.circle(img, (200, 200), 20, (0, 0, 255), -1)
cv2.imshow('tmp', img)
cv2.waitKey(0)
