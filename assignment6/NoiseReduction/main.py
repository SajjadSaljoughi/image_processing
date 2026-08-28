import numpy as np
import cv2


def calculate_average_3_in_3(image):
    rows, cols = image.shape
    result = np.zeros((rows, cols), np.uint8)
    kernel = np.ones((3, 3)) / 9
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            small = image[i - 1:i + 2, j - 1:j + 2]
            average = np.sum(kernel * small)
            result[i, j] = average
    return result


def calculate_average_5_in_5(image):
    rows, cols = image.shape
    result = np.zeros((rows, cols), np.uint8)
    kernel = np.ones((5, 5)) / 25
    for i in range(2, rows - 2):
        for j in range(2, cols - 2):
            small = image[i - 2:i + 3, j - 2:j + 3]
            average = np.sum(kernel * small)
            result[i, j] = average
    return result


def calculate_average_15_in_15(image):
    rows, cols = image.shape
    result = np.zeros((rows, cols), np.uint8)
    kernel = np.ones((15, 15)) / 325
    for i in range(7, rows - 7):
        for j in range(7, cols - 7):
            small = image[i - 7:i + 8, j - 7:j + 8]
            average = np.sum(kernel * small)
            result[i, j] = average
    return result


image1 = cv2.imread('input\\image1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('input\\image2.jpg', cv2.IMREAD_GRAYSCALE)
image3 = cv2.imread('input\\image3.png', cv2.IMREAD_GRAYSCALE)

result1_3_in_3 = calculate_average_3_in_3(image1)
result1_5_in_5 = calculate_average_5_in_5(image1)
result1_15_in_15 = calculate_average_15_in_15(image1)

result2_3_in_3 = calculate_average_3_in_3(image2)
result2_5_in_5 = calculate_average_5_in_5(image2)
result2_15_in_15 = calculate_average_15_in_15(image2)

result3_3_in_3 = calculate_average_3_in_3(image3)
result3_5_in_5 = calculate_average_5_in_5(image3)
result3_15_in_15 = calculate_average_15_in_15(image3)


cv2.imwrite('output\\result1_3_in_3.png', result1_3_in_3)
cv2.imwrite('output\\result1_5_in_5.png', result1_5_in_5)
cv2.imwrite('output\\result1_15_in_15.png', result1_15_in_15)

cv2.imwrite('output\\result2_3_in_3.png', result2_3_in_3)
cv2.imwrite('output\\result2_5_in_5.png', result2_5_in_5)
cv2.imwrite('output\\result2_15_in_15.png', result2_15_in_15)

cv2.imwrite('output\\result3_3_in_3.png', result3_3_in_3)
cv2.imwrite('output\\result3_5_in_5.png', result3_5_in_5)
cv2.imwrite('output\\result3_15_in_15.png', result3_15_in_15)

cv2.waitKey(0)
cv2.destroyAllWindows()
