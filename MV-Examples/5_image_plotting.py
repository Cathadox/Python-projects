import cv2 as cv
from matplotlib import pyplot as plt

lena = cv.imread("lenna.jpg", -1)

cv.imshow("Image", lena)
lena = cv.cvtColor(lena, cv.COLOR_BGR2RGB)

plt.xticks([]), plt.yticks([])
plt.imshow(lena)
plt.show()

cv.waitKey()
cv.destroyAllWindows()