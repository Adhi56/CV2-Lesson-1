import cv2

image = cv2.imread('/Users/adhi/Desktop/Open CV/Lesson1/pika.png', 1)

B, G, R = cv2.split(image)
cv2.imshow("original", image)
cv2.imshow("bluesaturatedimg", B)
cv2.imshow("greensaturatedimg", G)
cv2.imshow("redsaturatedimg", R)

cv2.waitKey(0)
cv2.destroyAllWindows()

