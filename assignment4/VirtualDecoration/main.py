import cv2

home = cv2.imread("input/home.jpg")
decore = cv2.imread("input/decore.jpg")
mask = cv2.imread("input/mask.jpg")
home_ = cv2.resize(home, (decore.shape[1], decore.shape[0]))
mask_ = mask.astype("float32")
result = mask_ / 255 * decore
mask_ = 255 - mask_
result += mask_ / 255 * home_
result = result.astype("uint8")
cv2.imwrite("output/result.jpg", result)
 