import numpy as np
import cv2 as cv

points = []
def click_event(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 10, (0,0, 255), 1)
        points.append((x,y))
        if len(points) >= 2:
            cv.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv.imshow("Image", img)

img = np.zeros((500,500,3), np.uint8)

cv.imshow("Image", img)

cv.setMouseCallback("Image", click_event)

cv.waitKey()
cv.destroyAllWindows()


