import cv2

def createTrackbar(trackbar_name, window_name, slider_max):
    cv2.createTrackbar(trackbar_name, window_name, 0, slider_max, onTrackbar)

def onTrackbar(val):
    pass

def getTrackbarValue(trackbarName, windowName):
    return int(cv2.getTrackbarPos(trackbarName, windowName) / 2) * 2 + 3

def adaptiveThreshold(frame, sliderMaxValue, adaptative, binary, trackbarVal):
    return cv2.adaptiveThreshold(frame, sliderMaxValue, adaptative, binary, trackbarVal, 0)

def denoise(frame, method, radius):
    kernel = cv2.getStructuringElement(method, (radius, radius))
    opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    return closing

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