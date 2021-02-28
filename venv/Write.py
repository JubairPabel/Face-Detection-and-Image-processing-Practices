import cv2 as cv

img = cv.imread("Ronaldo-1.jpg",1)

cv.imshow("Image",img)

#Create a new img

cv.imwrite("New_cr7.jpg", img )


cv.waitKey(0)