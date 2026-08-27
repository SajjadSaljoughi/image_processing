import random
import cv2
import imageio
import numpy as np

image = cv2.imread("input\\snow_landscape_2.jpg")
grayscale_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
height = grayscale_image.shape[0]
width = grayscale_image.shape[1]
num_flakes = 500
snow_flakes = []
for _ in range(num_flakes):
    x = random.randint(0,width)
    y = random.randint(0,height)
    speed = random.randint(1,2)
    size = random.randint(1,3)
    snow_flakes.append([x,y,speed,size])
gif_images = []
while True:
    frame = grayscale_image.copy()
    for flake in snow_flakes:
        x,y,speed,size = flake
        cv2.circle(frame,(x,y),size,255,-1)
        y += speed
        x += random.randint(-1, 1)
        if x < 0: x = width
        if x > width: x = 0
        if y > height:
            y = random.randint(-50, 0)
            x = random.randint(0,width)
        flake[0] = x
        flake[1] = y
    blur_mask = frame.copy()
    blur_mask = cv2.GaussianBlur(blur_mask, (5, 5), 0)
    frame = cv2.addWeighted(frame, 0.7, blur_mask, 0.3, 0)
    gif_images.append(frame)
    cv2.imshow("Snow Animation", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        imageio.mimsave('output\\snow_landscape_2.gif', gif_images, fps=30)
        break
