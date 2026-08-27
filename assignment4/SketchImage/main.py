import cv2

image = cv2.imread("input\\sajjad.jpg")
grayscale_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
inverted = 255 - grayscale_image
blurred = cv2.GaussianBlur(inverted,(21,21),0)
inverted_blurred = 255 - blurred
sketch = cv2.divide(grayscale_image, inverted_blurred,scale=256)
cv2.imwrite("output\\result.jpg",sketch)