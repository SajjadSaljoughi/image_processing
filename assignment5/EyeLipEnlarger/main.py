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

image = cv2.imread("input\\image.jpg")
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

# cv2.imshow("lip", image[194:226, 305:365])


lip = cv2.resize(
    lip,
    (108, 40)
)

lip_mask = cv2.resize(
    lip_mask,
    (108, 40),
    interpolation=cv2.INTER_NEAREST
)

left_eye = cv2.resize(
    left_eye,
    (68, 32)
)

left_eye_mask = cv2.resize(
    left_eye_mask,
    (68, 32),
    interpolation=cv2.INTER_NEAREST
)

right_eye = cv2.resize(
    right_eye,
    (60, 32)
)

right_eye_mask = cv2.resize(
    right_eye_mask,
    (60, 32),
    interpolation=cv2.INTER_NEAREST
)

left_eye_roi = image[
    194:226,
    233:301
]
image[
    194:226,
    233:301
] = put_filter(
    left_eye_roi,
    left_eye,
    left_eye_mask
)

right_eye_roi = image[
    194:226,
    305:365
]
image[
    194:226,
    305:365
] = put_filter(
    right_eye_roi,
    right_eye,
    right_eye_mask
)

lip_roi = image[
    258:298,
    251:359
]
image[
    258:298,
    251:359
] = put_filter(
    lip_roi,
    lip,
    lip_mask
)

cv2.imshow("image", image)
cv2.imwrite("output\\result.jpg", image)
cv2.waitKey()
cv2.destroyAllWindows()
