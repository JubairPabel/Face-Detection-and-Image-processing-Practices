import numpy as np

import cv2 as cv

img = np.zeros([300, 400, 3], np.uint8)

cv.imshow("Image", img)

cv.waitKey()

cv.destroyAllWindows()