import cv2
import numpy as np


def nothing(x):
    pass


frames = cv2.VideoCapture(0);

cv2.namedWindow("TRACKING")
cv2.createTrackbar("LH", "TRACKING", 0, 255, nothing)
cv2.createTrackbar("LS", "TRACKING", 0, 255, nothing)
cv2.createTrackbar("LV", "TRACKING", 0, 255, nothing)
cv2.createTrackbar("UH", "TRACKING", 255, 255, nothing)
cv2.createTrackbar("US", "TRACKING", 255, 255, nothing)
cv2.createTrackbar("UV", "TRACKING", 255, 255, nothing)

while True:
    _, frame = frames.read()

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("LH", "TRACKING")
    ls = cv2.getTrackbarPos("LS", "TRACKING")
    lv = cv2.getTrackbarPos("LV", "TRACKING")

    uh = cv2.getTrackbarPos("UH", "TRACKING")
    us = cv2.getTrackbarPos("US", "TRACKING")
    uv = cv2.getTrackbarPos("UV", "TRACKING")

    upper_color = np.array([lh, ls, lv])
    lower_color = np.array([uh, us, uv])

    mask = cv2.inRange(frame_hsv, upper_color, lower_color)
    kernel = np.zeros((5, 5), np.uint8)
    mask_close = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    result_mask = cv2.bitwise_and(frame, frame, mask=mask_close)

    cv2.imshow("frame_hsv", frame)
    cv2.imshow("mask", mask_close)
    cv2.imshow("result_mask", result_mask)

    key = cv2.waitKey(1)
    if key == 27:
        break;

frames.release()
cv2.destroyAllWindows()
