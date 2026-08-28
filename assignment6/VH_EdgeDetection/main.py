import cv2
import numpy as np

image = cv2.imread('input\\image.jpg', cv2.IMREAD_GRAYSCALE)
horizontal_filter = np.array([[-1, 0, 1],
                              [-1, 0, 1],
                              [-1, 0, 1]])

vertical_filter = np.array([[-1, -1, -1],
                            [0, 0, 0],
                            [1, 1, 1]])
rows, cols = image.shape
result = np.zeros((rows, cols), np.uint8)
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        small = image[i - 1:i + 2, j - 1:j + 2]
        avg = np.sum(horizontal_filter * small)
        avg2 = np.sum(vertical_filter * small)
        average = np.sqrt(pow(avg, 2.0) + pow(avg2, 2.0))
        result[i, j] = average

cv2.imwrite('output\\result.png', result)
# cv2.imshow('image', spider)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
