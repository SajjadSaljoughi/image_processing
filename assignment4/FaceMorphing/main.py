import cv2
import numpy as np

man_image = cv2.imread("input\\man.jpg")
woman_image = cv2.imread("input\\woman.jpg")
result_image_1 = man_image.astype(np.float32) * 3 / 4 + woman_image.astype(np.float32) / 4
result_image_2 = man_image.astype(np.float32)*2 / 4 + woman_image.astype(np.float32)*2 / 4
result_image_3 = man_image.astype(np.float32)/ 4 + woman_image.astype(np.float32)*3 / 4
result = np.concatenate((man_image,result_image_1.astype(np.uint8)\
                         ,result_image_2.astype(np.uint8)\
                        ,result_image_3.astype(np.uint8),woman_image),
                        axis=1)
cv2.imwrite("output\\face_morphing.jpg",result)
