import cv2

pic = cv2.imread('C:/Users/harish/pic_1.png')
cv2.imwrite('original.jpg',pic)

gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)

[ret,threshold] = cv2.threshold(gray, 128, 255,2)
cv2.imshow('Thresholded',threshold)
cv2.imwrite('Thresholded.jpg',threshold)
[ret, thresh1] = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Threshold',thresh1)
cv2.imwrite('Binary_Threshold.jpg',thresh1)

[ret,thresh2] = cv2.threshold(gray,125,255,cv2.THRESH_BINARY_INV)
[ret, thresh3] = cv2.threshold(gray, 27, 255, cv2.THRESH_BINARY)

bandThresh = cv2.bitwise_and(thresh2,thresh3)
cv2.imshow('Banded Threshold',bandThresh)
cv2.imwrite('Banded_Threshold.jpg',bandThresh)

[ret,thresh4] = cv2.threshold(gray,128,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
semiThresh = cv2.bitwise_and(gray,thresh4)
cv2.imshow('Semi-Thresholded',semiThresh)
cv2.imwrite('Semi-Threshold.jpg',semiThresh)

thresh5 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,101,10)
cv2.imshow('Adaptive Threshold', thresh5)
cv2.imwrite('Adaptive_Threshold.jpg',thresh5)

cv2.waitKey(0)