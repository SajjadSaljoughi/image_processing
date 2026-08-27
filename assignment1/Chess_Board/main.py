import cv2
white_image = cv2.imread("input\\white.jpg")
for i in range(16):
    for j in range(16):
        if i % 2 == 0 and j % 2 == 0:
            white_image[i*25:(i*25)+25,j*25:(j*25)+25] = 0
        elif i % 2 == 1 and j % 2 == 1:
            white_image[i*25:(i*25)+25,j*25:(j*25)+25] = 0
cv2.imwrite("output\\chess-board.jpg",white_image)
cv2.imshow("",white_image)
cv2.waitKey()
