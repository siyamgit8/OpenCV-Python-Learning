import cv2 as cv
import numpy as np

img = cv.imread('cv photos/teddy.jpg')

blank = np.zeros(img.shape[:2] , dtype= 'uint8')
# cv.imshow('blank' , blank)
rectangle  = cv.rectangle(blank.copy() , (30 , 30 ) , (370 , 370) , 255 , -1)

circle = cv.circle(blank.copy() , (img.shape[1]//2 , img.shape[0]//2) , 100 , 255 , -1)
# cv.imshow('mask',mask)

wierd_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('wierd shape ' , wierd_shape) 

masked = cv.bitwise_and(img , img,  mask = wierd_shape) # similar to the masked we used to do in capcut software 
cv.imshow('masked ( wired shaped ) -->' ,masked )





cv.waitKey(0)