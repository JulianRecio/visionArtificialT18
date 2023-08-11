import imutils
import cv2 as cv

video = cv.VideoCapture(0)

while (True) :
    ret, frame = video.read()

    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


grayFrame = cv.cvtColor(frame,cv.COLOR_BGRA2GRAY)
cv.imshow('grayFrame', grayFrame)
cv.waitKey(0)

ret1, thresh1 = cv.threshold(grayFrame, 0, 255, cv.THRESH_BINARY)
cv.imshow("Binary", thresh1)

def binary(val):
    ret1, thresh1 = cv.threshold(grayFrame, val, 255, cv.THRESH_BINARY)
    cv.imshow("Binary", thresh1)


cv.namedWindow('Binary')
cv.createTrackbar('Trackbar', 'Binary', 0, 255, binary)

binary(0)

cv.waitKey()

print("fin")

