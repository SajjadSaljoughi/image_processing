import cv2
image_1 = cv2.imread("input\\1.jpg")
image_2 = cv2.imread("input\\2.jpg")
monochrome_image_1 = cv2.cvtColor(image_1,cv2.COLOR_BGR2GRAY)
monochrome_image_2 = cv2.cvtColor(image_2,cv2.COLOR_BGR2GRAY)
for i in range(645):
    for j in range(645):
        monochrome_image_1[i,j] = 255 - monochrome_image_1[i,j]
for i in range(1202):
    for j in range(900):
        monochrome_image_2[i,j] = 255 - monochrome_image_2[i,j]
# cv2.imshow("",monochrome_image_2)
# cv2.waitKey()
cv2.imwrite("output\\woman.jpg",monochrome_image_1)
cv2.imwrite("output\\man.jpg",monochrome_image_2)