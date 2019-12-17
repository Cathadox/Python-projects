import cv2
import numpy as np

lenna = cv2.imread("lenna.jpg")

b, g, r = cv2.split(lenna)

lenna_mask = cv2.inRange(b, 128, 255)

b = cv2.bitwise_and(b, lenna_mask)
g = cv2.bitwise_and(g, lenna_mask)
r = cv2.bitwise_and(r, lenna_mask)

lenna_new = cv2.merge((b, g, r))

cv2.imshow("lenna_shaded", lenna_new)

cv2.waitKey()
cv2.destroyAllWindows()
