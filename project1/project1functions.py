import cv2

def createTrackbar(trackbar_name, window_name, slider_max):
    cv2.createTrackbar(trackbar_name, window_name, 0, slider_max, onTrackbar)

def onTrackbar(val):
    pass

def getTrackbarValue(trackbarName, windowName):
    return int(cv2.getTrackbarPos(trackbarName, windowName) / 2) * 2 + 3

def adaptiveThreshold(frame, sliderMaxValue, adaptative, binary, trackbarVal):
    return cv2.adaptiveThreshold(frame, sliderMaxValue, adaptative, binary, trackbarVal, 0)

import cv2

def denoise(frame, method, radius):
    # Obtener el tamaño del kernel
    ksize = (2 * radius + 1, 2 * radius + 1)
    # Calcular el anclaje para asegurarse de que esté dentro del tamaño del kernel
    anchor = (radius, radius)
    kernel = cv2.getStructuringElement(method, ksize, anchor)
    opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    return closing

def compareContours(contourComparable, savedConturs, maxDifference):
    for contour in savedConturs:
        if cv2.matchShapes(contourComparable, contour, cv2.CONTOURS_MATCH_I2, 0) < maxDifference:
            return True
        return False

def addLabel(contour, frame, label, color):
    moment = cv2.moments(contour)
    if moment["m00"] != 0:
        cX = int(moment["m10"] / moment["m00"])
        cY = int(moment["m01"] / moment["m00"])
        cv2.putText(frame, label, (cX - 31, cY), cv2.FONT_HERSHEY_PLAIN, 0.5, color, 2)

def getContourLabel(contourLabels, compareContour):
    for label, contour in contourLabels.items():
        if cv2.matchShapes(compareContour, contour, cv2.CONTOURS_MATCH_I2, 0) < 1:
            return label
        return "label not found"

#def binary(val):
#    ret1, thresh1 = cv.threshold(grayFrame, val, 255, cv.THRESH_BINARY)
#    cv.imshow("Binary", thresh1)
#
#binary(100)
#
#cv.namedWindow('Binary')
#cv.createTrackbar('Trackbar', 'Binary', 0, 255, binary)
#
#cv.waitKey()
#
##erosion
#
#kernel = np.ones((3,3), np.uint8)
#erosion = cv.morphologyEx(thresh1, cv.MORPH_ERODE, kernel)
#cv.imshow("erosion",erosion)
#
##close
#
#dilation = cv.morphologyEx(erosion, cv.MORPH_DILATE, kernel)
#cv.imshow("dilation",dilation)
#