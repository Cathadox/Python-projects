import cv2

lenna = cv2.imread("lenna.jpg")

b, g, r = cv2.split(lenna)

lenna_inrange_skin = cv2.inRange(lenna, (128, 128, 128), (255, 255, 255))

b = cv2.bitwise_and(b, lenna_inrange_skin)
g = cv2.bitwise_and(g, lenna_inrange_skin)
r = cv2.bitwise_and(r, lenna_inrange_skin)

lenna_new = cv2.merge((b, g, r))

cv2.imshow("lenna_skin_segment", lenna_new)

cv2.waitKey()
cv2.destroyAllWindows()
