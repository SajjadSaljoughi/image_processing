import numpy as np
import cv2
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel
from alignment import Alignment


def put_filter(background, foreground, mask):
    inverse_mask = cv2.bitwise_not(mask)

    background_part = cv2.bitwise_and(
        background,
        background,
        mask=inverse_mask
    )

    foreground_part = cv2.bitwise_and(
        foreground,
        foreground,
        mask=mask
    )

    result = cv2.add(
        background_part,
        foreground_part
    )

    return result


fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")
alignment = Alignment()

image = cv2.imread("input\\man.jpg")
fruit_image = cv2.imread("input\\strawberry.jpg")
color = (125, 255, 125)

boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
    alignment.get_lip_landmarks(pred)
    alignment.get_left_eye_landmarks(pred)
    alignment.get_right_eye_landmarks(pred)


lip, lip_mask = alignment.big_filter(
    image,
    "lip"
)

left_eye, left_eye_mask = alignment.big_filter(
    image,
    "left_eye"
)

right_eye, right_eye_mask = alignment.big_filter(
    image,
    "right_eye"
)


lip = cv2.resize(
    lip,
    (100, 50)
)

lip_mask = cv2.resize(
    lip_mask,
    (100, 50),
    interpolation=cv2.INTER_NEAREST
)

left_eye = cv2.resize(
    left_eye,
    (100, 50)
)

left_eye_mask = cv2.resize(
    left_eye_mask,
    (100, 50),
    interpolation=cv2.INTER_NEAREST
)

right_eye = cv2.resize(
    right_eye,
    (100, 50)
)

right_eye_mask = cv2.resize(
    right_eye_mask,
    (100, 50),
    interpolation=cv2.INTER_NEAREST
)

left_eye_roi = fruit_image[
    350:400,
    100:200
]
fruit_image[
    350:400,
    100:200
] = put_filter(
    left_eye_roi,
    left_eye,
    left_eye_mask
)

right_eye_roi = fruit_image[
    350:400,
    220:320
]
fruit_image[
    350:400,
    220:320
] = put_filter(
    right_eye_roi,
    right_eye,
    right_eye_mask
)

lip_roi = fruit_image[
    450:500,
    160:260
]
fruit_image[
    450:500,
    160:260
] = put_filter(
    lip_roi,
    lip,
    lip_mask
)

cv2.imshow("", fruit_image)
cv2.imwrite("output\\result.jpg", fruit_image)
cv2.waitKey()
cv2.destroyAllWindows()
