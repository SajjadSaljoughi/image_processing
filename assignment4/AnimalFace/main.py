import cv2
import numpy as np

image = cv2.imread("input/woman.jpg")
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
animal = cv2.imread("input/animal1.jpg", cv2.IMREAD_UNCHANGED)
grayscale_animal_image = cv2.cvtColor(animal, cv2.COLOR_BGR2GRAY)
face_detector = cv2.CascadeClassifier("haarcascade\\haarcascade_frontalface_default.xml")
faces = face_detector.detectMultiScale(grayscale_image)
for face in faces:
    x, y, w, h = face
    woman_face = image[y:y+h, x:x+w]
    animal = cv2.resize(animal,(w,h))
    animal_face = woman_face.astype(np.float32)*3/4 + animal.astype(np.float32)/4
    animal_face = animal_face.astype(np.uint8)
    image[y:y+h, x:x+w] = animal_face
cv2.imshow("result", image)
cv2.imwrite("output\\animal_face.jpg",image)
cv2.waitKey()
