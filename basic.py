import cv2 as cv

img = cv.imread("Ronaldo-1.jpg",1)

cv.imshow("image",img)

e = cv.waitKey()

if e == 27:
    cv.destroyAllWindows()
elif e == ord("s"):
    cv.imwrite("This is the new ronaldo", img)
    cv.destroyAllWindows()