import imutils
import numpy as np
import cv2 as cv
from project1functions import createTrackbar, getTrackbarValue, adaptiveThreshold, denoise

#reference_image1 = cv.imread("estrella.jpg")
#gray_reference1 = cv.cvtColor(reference_image1, cv.COLOR_BGR2GRAY)
#_, threshold_reference1 = cv.threshold(gray_reference1, 100, 255, cv.THRESH_BINARY)
#contours_reference1, _ = cv.findContours(threshold_reference1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#contours_reference1 = sorted(contours_reference1, key=cv.contourArea, reverse=True)
#reference_contour1 = contours_reference1[0]

video = cv.VideoCapture(0)
windowName = 'Window'
trackbarName = 'Trackbar'
sliderMaxValue = 151
cv.namedWindow(windowName)
video = cv.VideoCapture(0)

createTrackbar(trackbarName, windowName, sliderMaxValue)

while (True) :
    ret, frame = video.read()
    cv.imshow('frame', frame)

    grayFrame = cv.cvtColor(frame, cv.COLOR_BGRA2GRAY)
    cv.imshow('grayFrame', grayFrame)

    #ret1, thresh1 = cv.threshold(grayFrame, 100, 255, cv.THRESH_BINARY)
    #cv.imshow("Binary", thresh1)

    trackbarVal = getTrackbarValue(trackbarName=trackbarName, windowName=windowName)
    adaptFrame = adaptiveThreshold(frame=grayFrame, sliderMaxValue=sliderMaxValue, adaptative=cv.ADAPTIVE_THRESH_GAUSSIAN_C, binary=cv.THRESH_BINARY, trackbarVal=trackbarVal)

    frameDenoise = denoise(frame=adaptFrame, method=cv.MORPH_ELLIPSE,radius=5)

    cv.imshow('Window', frameDenoise)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cv.waitKey(0)
print("fin")

