import imutils
import numpy as np
import cv2 as cv
from project1functions import createTrackbar, getTrackbarValue, adaptiveThreshold, denoise, compareContours, addLabel, getContourLabel


greenColor = (0, 255, 0)
redColor = (0, 0, 255)

def main():
    windowName = "Detección"
    cv.namedWindow(windowName)
    video = cv.VideoCapture(0)

    createTrackbar("Threshold", windowName, 255)
    createTrackbar("Tamaño del kernel", windowName, 50)

    while True:
        ret, frame = video.read()
        # pasar a monocormatico
        grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        thresholdValue = cv.getTrackbarPos("Threshold", windowName)
        kernelSize = cv.getTrackbarPos("Tamaño del kernel", windowName)

        # threshold ajustable
        _, threshold = cv.threshold(grayFrame, thresholdValue, 255, 0)
        # operaciones morfológicas
        denoisedFrame = denoise(grayFrame, cv.MORPH_ELLIPSE, kernelSize)

        # cv.imshow("xd",denoisedFrame)

        contours,_ = cv.findContours(denoisedFrame, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        contoursDict = {}
        savedContours = contoursDict.values()

        if len(contours) > 0:
            for contour in contours:
                contourColor = greenColor if compareContours(contour, savedContours, 1) else redColor
                cv.drawContours(denoisedFrame, [contour], -1, contourColor, 3)
                cv.drawContours(frame, [contour], -1, contourColor, 3)
                addLabel(contour, frame, getContourLabel(contoursDict, contour), contourColor)

        cv.imshow(windowName, frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()

main()
