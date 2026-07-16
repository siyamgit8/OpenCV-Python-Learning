import cv2 as cv
import numpy as np

img = cv.imread('cv photos/teddy.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

rectangle  = cv.rectangle(blank.copy() , (30 , 30 ) , (370 , 370) , 255 , -1) # this function takes five arguments, first is the image, second is the top left corner of the rectangle, third is the bottom right corner of the rectangle, fourth is the color of the rectangle and fifth is the thickness of the rectangle. The thickness can be negative which means that the rectangle will be filled with color.
circle = cv.circle(blank.copy() , (250 , 250) , 150 , 255 , -1) # this function takes five arguments, first is the image, second is the center of the circle, third is the radius of the circle, fourth is the color of the circle and fifth is the thickness of the circle. The thickness can be negative which means that the circle will be filled with color.
cv.imshow('Rectangle' , rectangle)
cv.imshow('Circle' , circle)

# Bitwise AND
bitwise_and = cv.bitwise_and(rectangle , circle) # this function takes two arguments
cv.imshow('Bitwise AND' , bitwise_and) # this function takes two arguments, first is the first image and second is the second image. The function performs a bitwise AND operation on the two images. The result is an image where the pixels are white if both the corresponding pixels in the two images are white, otherwise the pixel is black.

# Bitwise OR
bitwise_or = cv.bitwise_or(rectangle , circle) # this function takes two arguments, first is the first image and second is the second image. The function performs a bitwise OR operation on the two images. The result is an image where the pixels are white if either of the corresponding pixels in the two images is white, otherwise the pixel is black.
cv.imshow('Bitwise OR' , bitwise_or)

# Bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle , circle) # this function takes two arguments, first is the first image and second is the second image. The function performs a bitwise XOR operation on the two images. The result is an image where the pixels are white if either of the corresponding pixels in the two images is white, but not both, otherwise the pixel is black.
cv.imshow('Bitwise XOR' , bitwise_xor) # return the region where the two images are different. or not intersecting 

# Bitwise not
bitwise_not = cv.bitwise_not(rectangle , circle)
cv.imshow('Bitwise_NOT' , bitwise_not )

cv.imshow('Image', img)
cv.waitKey(0)