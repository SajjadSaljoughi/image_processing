import cv2
import matplotlib.pyplot as plt
import numpy as np

from histogram import histogram

image = cv2.imread('input\\test.jpg')
resized_image = cv2.resize(image, (600, 600))
result = histogram(resized_image)
# plt.plot(result)
# plt.savefig('output\\plot.png')
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
plt.hist(gray.ravel(), 256, (0, 256))
plt.savefig('output\\hist.png')
# label = np.arange(256)
# plt.bar(label, result)
# plt.savefig('output\\bar.png')
