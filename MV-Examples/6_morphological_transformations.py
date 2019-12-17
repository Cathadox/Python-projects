import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

mnms_original = cv.imread("mnms.jpg", cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(mnms_original, 220, 255, cv.THRESH_BINARY_INV)
kernel = np.ones((10, 10), np.uint8)

mask_dilated = cv.dilate(mask, kernel, iterations=1)
mask_eroded = cv.erode(mask, kernel, iterations=1)
mask_closed = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
mask_opened = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
mask_gradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)
mask_tophatted = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel)

titles = ['original', 'masked', 'dilated mask', 'eroded mask', 'closed mask', 'opened mask', 'gradient mask', 'tophat mask']
images = [mnms_original, mask, mask_dilated, mask_eroded, mask_closed, mask_opened, mask_gradient, mask_tophatted]

for i in range(8):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
