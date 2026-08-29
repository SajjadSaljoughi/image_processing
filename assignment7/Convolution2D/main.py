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

result = cv2.filter2D(image, -1, kernel5)

# cv2.imshow("result", result)
cv2.imwrite("output\\my_filter.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()