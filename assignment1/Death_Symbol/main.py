import cv2
image_1 = cv2.imread("input\\Thomas_Edison.jpg")
image_2 = cv2.imread("input\\Graham_Bell.jpg")
grayscale_image_1 = cv2.cvtColor(image_1,cv2.COLOR_BGR2GRAY)
grayscale_image_2 = cv2.cvtColor(image_2,cv2.COLOR_BGR2GRAY)
h = 200
w = 200
h2 = 100
w2 = 100
for i in range(0,h):
    for j in range(0,w):
        if i <= h2 and j >= w2:
            grayscale_image_1[i,j] = 0
            grayscale_image_2[i,j] = 0
        elif i > h2:
            grayscale_image_1[i,j] = 0
            grayscale_image_2[i,j] = 0
    w -= 1
    w2 -= 1

# cv2.imshow("",grayscale_image)
# cv2.waitKey()
cv2.imwrite("output\\death_Thomas_Edison.jpg",grayscale_image_1)
cv2.imwrite("output\\death_Graham_Bell.jpg",grayscale_image_2)