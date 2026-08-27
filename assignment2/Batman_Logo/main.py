import cv2
import numpy as np
image = cv2.imread("input\\batman.jpg")
height = image.shape[0]
width = image.shape[1]
grayscale_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
threshold = 137
_,monochrome_image = cv2.threshold(grayscale_image,threshold,255,cv2.THRESH_BINARY_INV)
width = int(width / 2) - 130
height = height - 80
cv2.putText(monochrome_image,"BATMAN",(width,height),\
            cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,255,5)
cv2.imwrite("output\\batman-logo.jpg",monochrome_image)
cv2.imshow("",monochrome_image)
cv2.waitKey()