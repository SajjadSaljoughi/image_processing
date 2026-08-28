import cv2
import numpy as np


def calculate_average(image, type_image="spider",
                      vertical_filter=None,
                      horizontal_filter=None,
                      kernel_filter=None):
    rows, cols = image.shape
    result = np.zeros((rows, cols), np.uint8)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            small = image[i - 1:i + 2, j - 1:j + 2]
            if type_image == "spider":
                avg = np.sum(horizontal_filter * small)
                avg2 = np.sum(vertical_filter * small)
                average = np.sqrt(pow(avg, 2.0) + pow(avg2, 2.0))
            elif type_image == "lion":
                average = np.abs(np.sum(kernel_filter * small))
            result[i, j] = average
    return result


spider_image = cv2.imread('input\\image1.jpg', cv2.IMREAD_GRAYSCALE)
lion_image = cv2.imread('input\\image2.jpg', cv2.IMREAD_GRAYSCALE)

kernel = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
])

horizontal_filter = np.array([[-1, 0, 1],
                              [-1, 0, 1],
                              [-1, 0, 1]])

vertical_filter = np.array([[-1, -1, -1],
                            [0, 0, 0],
                            [1, 1, 1]])

lion = calculate_average(lion_image, type_image="lion", kernel_filter=kernel)
spider = calculate_average(spider_image, type_image="spider", vertical_filter=vertical_filter,
                           horizontal_filter=horizontal_filter)

cv2.imwrite('output\\lion.png', lion)
cv2.imwrite('output\\spider.png', spider)
# cv2.imshow('image', spider)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
