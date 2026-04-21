import cv2
import os

image = cv2.imread('/Users/adhi/Desktop/Open CV/Lesson1/pika.png', 0)
cv2.imshow("window", image)

path = '/Users/adhi/Desktop/Open CV/Lesson1'
os.chdir(path)

cv2.imwrite("blackandWhite.png",image)
print("img saved successfully")

cv2.waitKey(5000)
cv2.destroyAllWindows()
