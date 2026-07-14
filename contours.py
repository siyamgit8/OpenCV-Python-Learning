import cv2 as cv 
import numpy as np 

img = cv.imread('cv photos/img_600x800.jpg')

cv.imshow('image' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

cv.imshow('gray ' ,gray )

blank = np.zeros(img.shape , dtype = 'uint8') # np.zeros is a function that is used to create an array of zeros. It takes two arguments: the shape of the array and the data type of the array. The shape of the array is specified as a tuple of integers, where each integer represents the size of the corresponding dimension of the array. The data type of the array is specified as a string, where 'uint8' represents an unsigned 8-bit integer.
cv.imshow('blank ' , blank)

blur = cv.GaussianBlur(gray , (5 , 5), cv.BORDER_DEFAULT) # GaussianBlur is a function that is used to blur an image. It takes three arguments: the image, the kernel size, and the border type. The kernel size is used to determine the size of the filter that is applied to the image, and the border type is used to determine how the borders of the image are handled. The BORDER_DEFAULT border type is used to apply a default border to the image.

canny = cv.Canny(blur , 125 , 175) # Canny is a function that is used to detect edges in an image. It takes three arguments: the image, the lower threshold, and the upper threshold. The lower threshold is used to determine which pixels are considered to be edges, and the upper threshold is used to determine which pixels are considered to be non-edges. The Canny function uses a multi-stage algorithm to detect edges in an image.
cv.imshow('canny ' , canny)

ret , thres = cv.threshold(gray , 125 , 255 , cv.THRESH_BINARY) # threshold is a function that is used to convert an image to a binary image. It takes four arguments: the image, the threshold value, the maximum value, and the threshold type. The threshold value is used to determine which pixels are considered to be foreground pixels, and the maximum value is used to determine the value of the foreground pixels. The THRESH_BINARY threshold type is used to convert the image to a binary image.
cv.imshow('thres ' , thres)

contours , hierarchies = cv.findContours(thres , cv.RETR_LIST , cv.CHAIN_APPROX_NONE) # findContours is a function that is used to find contours in an image. It takes three arguments: the image, the contour retrieval mode, and the contour approximation method. The contour retrieval mode is used to determine how the contours are retrieved from the image, and the contour approximation method is used to determine how the contours are approximated. The RETR_LIST mode retrieves all of the contours in the image, and the CHAIN_APPROX_NONE method approximates the contours using a simple chain of points.
print(f'{len(contours)} contours found!') # f' is a string formatting method that is used to insert variables into a string. The {len(contours)} expression is used to insert the length of the contours list into the string.

cv.drawContours(blank , contours , -1 , (0 , 0 , 255) , 1) # drawContours is a function that is used to draw contours on an image. It takes five arguments: the image, the contours, the contour index, the color, and the thickness. The contour index is used to determine which contour to draw, and the color is used to determine the color of the contour. The thickness is used to determine the thickness of the contour.
cv.imshow('contours drawn ' , blank)



cv.waitKey(0)