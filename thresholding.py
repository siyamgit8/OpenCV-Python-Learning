import cv2 as cv
import numpy as np

img = cv.imread('cv photos/teddy.jpg')

# Simple Thresholding 
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('GRAY'  , gray)

threshold  , thresh = cv.threshold(gray  , 150 , 255 , cv.THRESH_BINARY)
cv.imshow('thresholded' , thresh)

threshold  , thresh_inv = cv.threshold(gray  , 150 , 255 , cv.THRESH_BINARY_INV)
cv.imshow('inverse threshold ' , thresh_inv)

# Adaptive THRESHOLDING
adaptive_thresh = cv.adaptiveThreshold(gray , 255  , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY_INV , 11 , 3 )
cv.imshow('adaptive ' , adaptive_thresh)

# cv.imshow('Image', img)
cv.waitKey(0)