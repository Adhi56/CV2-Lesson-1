import cv2

image = cv2.imread('/Users/adhi/Desktop/Open CV/Lesson1/pika.png', 0)
cv2.imshow('window', image)

cv2.waitKey(0)
cv2.destroyAllWindows()