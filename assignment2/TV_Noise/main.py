import cv2
import numpy as np
import imageio
image = cv2.imread("input\\tv.jpg")
grayscale_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gif_images = []
while True:
    noise = np.random.random((180,240)) * 255
    noise = np.array(noise,dtype=np.uint8)
    grayscale_image[150:330,220:460] = noise
    gif_images.append(grayscale_image.copy())
    cv2.imshow("",grayscale_image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        imageio.mimsave('output\\tv_noise.gif', gif_images, fps=30)
        break