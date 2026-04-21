import cv2

#cv2.IMREAD_COLOR (1) => Specify to load the image in color. excludes transparency
#cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged

image = cv2.imread('/Users/adhi/Desktop/Open CV/Lesson1/pika.png', 1)
cv2.imshow('output', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

