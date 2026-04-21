import cv2

image = cv2.imread("/Users/adhi/Desktop/Open CV/Lesson1/pokemon.png", 1)

B, G, R = cv2.split(image)

cv2.imshow("original", image)
cv2.imshow("bluesaturated", B)
cv2.imshow("greensaturated", G)
cv2.imshow("redsaturated", R)

cv2.waitKey(0)
cv2.destroyAllWindows()
