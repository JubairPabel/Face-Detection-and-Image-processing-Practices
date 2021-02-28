import cv2 as cv

img = cv.imread("lena.jpg", 1)

img = cv.line(img, (0, 255), (255, 255), (255, 0, 0), thickness=20)
img = cv.arrowedLine(img, (0, 0), (255, 255), (0, 0, 255), thickness=10)

cv.imshow("Image",img)

cv.waitKey(0)
cv.destroyAllWindows()