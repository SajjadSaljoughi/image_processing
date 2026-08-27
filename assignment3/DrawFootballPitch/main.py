import cv2
import numpy as np
height = 400
width = 800
white_image = np.ones((height,width,3),np.uint8) * 255
for i in range(10):
    if i % 2 == 0:
        white_image[:,i*(width // 10):i*(width // 10)+(width // 10)] = (0,255,0)
    else:
        white_image[:,i*(width // 10):i*(width // 10)+(width // 10)] = (0,155,0)
cv2.rectangle(white_image,(25,25),(width - 25,height - 25),(255,255,255),4)
cv2.line(white_image,(width//2,25),(width//2,height - 25)\
         ,(255,255,255),4)
cv2.circle(white_image,(width//2,height//2),4,(255,255,255),4)
cv2.circle(white_image,(width//2,height//2),75,(255,255,255),4)
cv2.rectangle(white_image,(25,100),(125,300),(255,255,255),4)
cv2.rectangle(white_image,(25,150),(75,250),(255,255,255),4)
cv2.rectangle(white_image,(width - 100 - 25,100),(width - 25,300),(255,255,255),4)
cv2.rectangle(white_image,(width - 25 - 50,150),(width - 25,250),(255,255,255),4)
cv2.imwrite("output\\Football Pitch.jpg",white_image)
cv2.imshow("",white_image)
cv2.waitKey()