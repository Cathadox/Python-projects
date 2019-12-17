import cv2
import numpy as np

lenna = cv2.imread("lenna.jpg")

lenna_inrange_mask = cv2.inRange(lenna, (128, 0, 0), (255, 255, 255))

mask = cv2.merge(lenna, lenna_inrange_mask)
masked = cv2.bitwise_and(lenna, mask)

cv2.imshow("lenna_new", masked)
cv2.waitKey()
cv2.destroyAllWindows()