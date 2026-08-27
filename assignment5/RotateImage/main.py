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

image = cv2.imread("input\\rotated-man.jpg")
color = (125, 255, 125)

boxes, scores = fd.inference(image)

image_rotated = cv2.rotate(image,cv2.ROTATE_180)

for pred in fa.get_landmarks(image_rotated, boxes):
    alignment.get_lip_landmarks(pred)
    alignment.get_left_eye_landmarks(pred)
    alignment.get_right_eye_landmarks(pred)

lip, lip_mask = alignment.big_filter(
    image_rotated,
    "lip"
)

left_eye, left_eye_mask = alignment.big_filter(
    image_rotated,
    "left_eye"
)

right_eye, right_eye_mask = alignment.big_filter(
    image_rotated,
    "right_eye"
)

image = cv2.resize(image, (800, 600))

lip = cv2.resize(
    lip,
    (150, 60)
)

lip_mask = cv2.resize(
    lip_mask,
    (150, 60),
    interpolation=cv2.INTER_NEAREST
)

left_eye = cv2.resize(
    left_eye,
    (100, 40)
)

left_eye_mask = cv2.resize(
    left_eye_mask,
    (100, 40),
    interpolation=cv2.INTER_NEAREST
)

right_eye = cv2.resize(
    right_eye,
    (100, 40)
)

right_eye_mask = cv2.resize(
    right_eye_mask,
    (100, 40),
    interpolation=cv2.INTER_NEAREST
)

left_eye_roi = image[340:380,250:350]
right_eye_roi = image[340:380,450:550]
lip_roi = image[175:235,320:470]

image[340:380,250:350] = put_filter(
    left_eye_roi,
    left_eye,
    left_eye_mask
)
image[340:380,450:550] = put_filter(
    right_eye_roi,
    right_eye,
    right_eye_mask
)
image[175:235,320:470] = put_filter(
    lip_roi,
    lip,
    lip_mask
)


cv2.imshow("image", image)
cv2.imwrite("output\\result.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
