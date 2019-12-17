import cv2
import numpy as np

lenna = cv2.imread("lenna.jpg")

cv2.imshow("lenna_original", lenna)

cv2.waitKey()

lenna[:, :, 0] = (lenna[:, :, 0] * 1.5).astype(int).clip(0, 255)

cv2.imshow("lenna_new", lenna)

cv2.waitKey()
