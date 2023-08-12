import imutils
import numpy as np
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

binary(100)

cv.namedWindow('Binary')
cv.createTrackbar('Trackbar', 'Binary', 0, 255, binary)

cv.waitKey()

#erosion

kernel = np.ones((3,3), np.uint8)
erosion = cv.morphologyEx(thresh1, cv.MORPH_ERODE, kernel)
cv.imshow("erosion",erosion)

#close

dilation = cv.morphologyEx(erosion, cv.MORPH_DILATE, kernel)
cv.imshow("dilation",dilation)


cv.waitKey(0)
print("fin")

