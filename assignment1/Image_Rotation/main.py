import cv2
image_1 = cv2.imread("input\\3.jpg")
monochrome_image_1 = cv2.cvtColor(image_1,cv2.COLOR_BGR2GRAY)
rotate = monochrome_image_1.copy()
height , width = monochrome_image_1.shape
for i in range(height):
    for j in range(width):
        rotate[i,j] = monochrome_image_1[height - 1 - i,width - 1 - j]
# cv2.imshow("",after_rotate)
# cv2.waitKey()
cv2.imwrite("output\\rotate.jpg",rotate)