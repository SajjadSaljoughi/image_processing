import cv2
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel
from alignment import Alignment

fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")
alignment = Alignment()

image = cv2.imread("input\\image.png")

color = (125, 255, 125)

boxes, scores = fd.inference(image)

center_left_eye = None
center_right_eye = None

for pred in fa.get_landmarks(image, boxes):
    center_left_eye = pred[38]
    center_right_eye = pred[88]

result = alignment.alignment_procedure(image,center_left_eye,center_right_eye)

cv2.imshow("", result)
cv2.imwrite("output\\result.jpg", result)
cv2.waitKey()
cv2.destroyAllWindows()
