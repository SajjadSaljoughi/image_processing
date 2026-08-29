import cv2
import numpy as np

kernel = np.ones((15, 15)) / 325

image = cv2.imread("input\\1.tif")

result = cv2.filter2D(image, -1, kernel)

# cv2.imshow("result", result)
cv2.imwrite("output\\result.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
