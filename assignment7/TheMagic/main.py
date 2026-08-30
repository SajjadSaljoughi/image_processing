import cv2
import numpy as np

kernel1 = np.ones((5, 5)) * 0.04
kernel2 = np.ones((5, 5)) * 1
kernel3 = np.ones((5, 5)) * 5
kernel4 = np.ones((3, 3)) * 0.04
kernel5 = np.ones((3, 3)) * 1
kernel6 = np.ones((3, 3)) * 5

image = cv2.imread("input\\1.tif")

result1 = cv2.filter2D(image, -1, kernel1)
result2 = cv2.filter2D(image, -1, kernel2)
result3 = cv2.filter2D(image, -1, kernel3)
result4 = cv2.filter2D(image, -1, kernel4)
result5 = cv2.filter2D(image, -1, kernel5)
result6 = cv2.filter2D(image, -1, kernel6)

result = np.hstack((image, result1, result2, result3, result4, result5, result6))

cv2.imwrite("output\\result1.jpg", result1)
cv2.imwrite("output\\result2.jpg", result2)
cv2.imwrite("output\\result3.jpg", result3)
cv2.imwrite("output\\result4.jpg", result4)
cv2.imwrite("output\\result5.jpg", result5)
cv2.imwrite("output\\result6.jpg", result6)
cv2.imwrite("output\\result.jpg", result)
