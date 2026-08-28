import cv2
import numpy as np

image = cv2.imread('input\\image.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = image.shape
blur_filter = np.ones((15, 15)) / 325
result = np.zeros((rows, cols), np.uint8)
for i in range(7, rows - 7):
    for j in range(7, cols - 7):
        if image[i, j] <= 150:
            small = image[i - 7:i + 8, j - 7:j + 8]
            average = np.sum(small * blur_filter)
        else:
            average = image[i, j]
        result[i, j] = average

cv2.imwrite('output\\result.png', result)
cv2.imshow('image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
