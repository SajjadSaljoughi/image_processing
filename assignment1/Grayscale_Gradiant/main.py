import cv2
white_image = cv2.imread("input\\white.jpg")
grayscale_image = cv2.cvtColor(white_image,cv2.COLOR_BGR2GRAY)
for i in range(400):
    grayscale_image[i,0:400] = 255 - (i*255//400)
cv2.imshow("",grayscale_image)
cv2.waitKey()
cv2.imwrite("output\\gradiant_image.jpg",grayscale_image)