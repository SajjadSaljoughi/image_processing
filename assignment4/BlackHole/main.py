import cv2
import numpy as np
import os

def noise_reduce(image_list):
    result_image = np.zeros((1000,1000,3))
    for image in image_list:
        result_image += image.astype(np.float32)
    result_image = result_image / 5
    return result_image.astype(np.uint8)
black_hole_result = np.zeros((2000,2000,3),np.uint8)
for i in range(1,5):
    image_path = os.listdir(f"input\\{i}")
    images = []
    for path in image_path:
        image = cv2.imread(f"input\\{i}\\{path}")
        images.append(image)
    result = noise_reduce(images)
    if i == 1:
        black_hole_result[0:1000,0:1000] = result
    elif i == 2:
        black_hole_result[0:1000,1000:2000] = result
    elif i == 3:
        black_hole_result[1000:2000,0:1000] = result
    elif i == 4:
        black_hole_result[1000:2000,1000:2000] = result   

cv2.imshow("",black_hole_result)
cv2.imwrite("output\\result.jpg",black_hole_result)
cv2.waitKey()