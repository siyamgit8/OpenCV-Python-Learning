import cv2 as cv
import numpy as np

img = cv.imread('cv photos/teddy.jpg')

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)

# laplation 
lap = cv.Laplacian(gray , cv.CV_64F) # computes the gradient of the image , all pixels values are transformed to the absolute value of the image and converted to uint8
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian' , lap)

# Sobel 
sobelx = cv.Sobel(gray  , cv.CV_64F , 1 , 0)
sobely = cv.Sobel(gray , cv.CV_64F , 0 , 1 )

cv.imshow('sobel x ' , sobelx)
cv.imshow('sobel y ' , sobely)
combined_sobel = cv.bitwise_and(sobelx , sobely)
cv.imshow('combined ' , combined_sobel) 

canny = cv.Canny(gray , 150 , 175 )
cv.imshow('canny', canny) # uses sobel for its one of its methods 

# cv.imshow('Image', img)
cv.waitKey(0)    