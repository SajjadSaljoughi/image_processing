import cv2
import numpy as np

# 1. Edge detection filter
kernel1 = np.array([[-1 , -1 , -1],
                   [-1 ,  8 , -1],
                   [-1 , -1 , -1]])

# 2. Sharpening filter
kernel2 = np.array([[0  , -1 ,  0],
                   [-1 ,  5 , -1],
                   [0  , -1 ,  0]])

# 3. Emboss filter
kernel3 = np.array([[-2 , -1 ,  0],
                   [-1 ,  1 ,  1],
                   [0  ,  1 ,  2]])

# 4. Identity filter
kernel4 = np.array([[0  ,  0 ,  0],
                   [0  ,  1 ,  0],
                   [0  ,  0 ,  0]])

# 5. Your filter
kernel5 = np.array([[0  ,  -1 ,  0],
                   [-1  ,  4 ,  -1],
                   [0  ,  -1 ,  0]])

image = cv2.imread("input\\test.jpg")

result1 = cv2.filter2D(image, -1, kernel1)
result2 = cv2.filter2D(image, -1, kernel2)
result3 = cv2.filter2D(image, -1, kernel3)
result4 = cv2.filter2D(image, -1, kernel4)
result5 = cv2.filter2D(image, -1, kernel5)

image1 = np.hstack((image,result1))
image2 = np.hstack((image,result2))
image3 = np.hstack((image,result3))
image4 = np.hstack((image,result4))
image5 = np.hstack((image,result5))

result = np.hstack((image, result1, result2, result3, result4, result5))


cv2.imwrite("output\\edge_detection.jpg", image1)
cv2.imwrite("output\\sharpening.jpg", image2)
cv2.imwrite("output\\emboss.jpg", image3)
cv2.imwrite("output\\identity.jpg", image4)
cv2.imwrite("output\\my_filter.jpg", image5)
cv2.imwrite("output\\result.jpg", result)
