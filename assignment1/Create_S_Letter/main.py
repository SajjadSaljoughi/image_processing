import cv2
white_image = cv2.imread("input\\white.jpg")
grayscale_image = cv2.cvtColor(white_image,cv2.COLOR_BGR2GRAY)
grayscale_image[100:275,100:300] = 0
grayscale_image[125:175,125:300] = 255
grayscale_image[200:250,100:275] = 255
cv2.imshow("",grayscale_image)
cv2.waitKey()
cv2.imwrite("output\\first_letter_my_name.jpg",grayscale_image)