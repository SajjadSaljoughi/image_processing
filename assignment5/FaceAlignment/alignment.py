import numpy as np
import cv2
import  math
from PIL import Image


class Alignment:
    def __init__(self):
        self.lips_landmarks = []
        self.left_eye = []
        self.right_eye = []
        self.filter = ""

    def get_lip_landmarks(self, pred):
        for i in [52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64]:
            self.lips_landmarks.append(pred[i])
        self.lips_landmarks = np.array(self.lips_landmarks, dtype=np.int64)

    def get_left_eye_landmarks(self, pred):
        for i in [35, 36, 33, 37, 39, 42, 40, 41]:
            self.left_eye.append(pred[i])
        self.left_eye = np.array(self.left_eye, dtype=np.int64)

    def get_right_eye_landmarks(self, pred):
        for i in [89, 90, 87, 91, 93, 96, 94, 95]:
            self.right_eye.append(pred[i])
        self.right_eye = np.array(self.right_eye, dtype=np.int64)

    def big_filter(self, image, type_filter):
        if type_filter == "lip":
            self.filter = self.lips_landmarks
        elif type_filter == "left_eye":
            self.filter = self.left_eye
        elif type_filter == "right_eye":
            self.filter = self.right_eye
        x, y, w, h = cv2.boundingRect(self.filter)
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        cv2.drawContours(mask, [self.filter], -1, 255, -1)
        result = cv2.bitwise_and(
            image,
            image,
            mask=mask
        )
        result = result[y:y + h, x:x + w]
        mask = mask[y:y + h, x:x + w]
        return result, mask

    @staticmethod
    def euclidean_distance(source_representation, test_representation):
        euclidean_distance = source_representation - test_representation
        euclidean_distance = np.sum(np.multiply(euclidean_distance, euclidean_distance))
        euclidean_distance = np.sqrt(euclidean_distance)
        return euclidean_distance

    def alignment_procedure(self, img, left_eye, right_eye):

        #this function aligns given face in img based on left and right eye coordinates

        left_eye_x, left_eye_y = left_eye
        right_eye_x, right_eye_y = right_eye

        #-----------------------
        #find rotation direction

        if left_eye_y > right_eye_y:
            point_3rd = (right_eye_x, left_eye_y)
            direction = -1 #rotate same direction to clock
        else:
            point_3rd = (left_eye_x, right_eye_y)
            direction = 1 #rotate inverse direction of clock

        #-----------------------
        #find length of triangle edges

        a = self.euclidean_distance(np.array(left_eye), np.array(point_3rd))
        b = self.euclidean_distance(np.array(right_eye), np.array(point_3rd))
        c = self.euclidean_distance(np.array(right_eye), np.array(left_eye))

        #-----------------------

        #apply cosine rule

        if b != 0 and c != 0: #this multiplication causes division by zero in cos_a calculation

            cos_a = (b*b + c*c - a*a)/(2*b*c)
            angle = np.arccos(cos_a) #angle in radian
            angle = (angle * 180) / math.pi #radian to degree

            #-----------------------
            #rotate base image

            if direction == -1:
                angle = 90 - angle

            img = Image.fromarray(img)
            img = np.array(img.rotate(direction * angle))

        #-----------------------

        return img #return img anyway