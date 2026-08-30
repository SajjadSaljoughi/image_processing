import cv2
import numpy as np

image1 = cv2.imread("input/image1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("input/image2.jpg", cv2.IMREAD_GRAYSCALE)
image3 = cv2.imread("input/image3.jpg", cv2.IMREAD_GRAYSCALE)

equalize1 = cv2.equalizeHist(image1)
cl1 = cv2.createCLAHE(0)
clahe1 = cl1.apply(image1)
result1 = np.hstack((image1, equalize1, clahe1))

equalize2 = cv2.equalizeHist(image2)
cl2 = cv2.createCLAHE(0)
clahe2 = cl2.apply(image2)
result2 = np.hstack((image2, equalize2, clahe2))

equalize3 = cv2.equalizeHist(image3)
cl3 = cv2.createCLAHE(0)
clahe3 = cl1.apply(image3)
result3 = np.hstack((image3, equalize3, clahe3))

cv2.imwrite("output/result1.jpg", result1)
cv2.imwrite("output/result2.jpg", result2)
cv2.imwrite("output/result3.jpg", result3)
