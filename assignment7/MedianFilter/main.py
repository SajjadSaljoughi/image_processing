import cv2
import numpy as np

image1 = cv2.imread("input\\image1.jpg")
image2 = cv2.imread("input\\image2.jpg")
image3 = cv2.imread("input\\image3.png")
image4 = cv2.imread("input\\image4.jpg")
image5 = cv2.imread("input\\image5.png")
image6 = cv2.imread("input\\image6.png")

medianBlur_image1 = cv2.medianBlur(image1, 7)
medianBlur_image2 = cv2.medianBlur(image2, 7)
medianBlur_image3 = cv2.medianBlur(image3, 7)
medianBlur_image4 = cv2.medianBlur(image4, 7)
medianBlur_image5 = cv2.medianBlur(image5, 15)
medianBlur_image6 = cv2.medianBlur(image6, 7)

result1 = np.hstack((image1,medianBlur_image1))
result2 = np.hstack((image2,medianBlur_image2))
result3 = np.hstack((image3,medianBlur_image3))
result4 = np.hstack((image4,medianBlur_image4))
result5 = np.hstack((image5,medianBlur_image5))
result6 = np.hstack((image6,medianBlur_image6))

cv2.imwrite("output\\result1.jpg", result1)
cv2.imwrite("output\\result2.jpg", result2)
cv2.imwrite("output\\result3.jpg", result3)
cv2.imwrite("output\\result4.jpg", result4)
cv2.imwrite("output\\result5.jpg", result5)
cv2.imwrite("output\\result6.jpg", result6)
