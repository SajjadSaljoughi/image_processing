import cv2

image_1 = cv2.imread("input\\image_1.png")
grayscale_image_1 = cv2.cvtColor(image_1,cv2.COLOR_BGR2RGB)
image_2 = cv2.imread("input\\image_2.png")
grayscale_image_2 = cv2.cvtColor(image_2,cv2.COLOR_BGR2RGB)
grayscale_image_1 = 255 - grayscale_image_1
grayscale_image_2 = 255 - grayscale_image_2
result = cv2.subtract(grayscale_image_1,grayscale_image_2)
cv2.imwrite("output\\result.jpg",result)