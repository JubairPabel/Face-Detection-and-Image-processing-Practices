import cv2 as cv

cap = cv.VideoCapture(1)

while(cap.isOpened()):
    ret, frame = cap.read()

    cv.imshow("Frmae", frame)

    if cv.waitKey(1) & 0xFF==ord("e"):
        break

cap.release()
cv.destroyAllWindows()