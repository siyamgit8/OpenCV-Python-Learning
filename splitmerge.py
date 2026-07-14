import cv2 as cv 
import numpy as np

img = cv.imread('cv photos/img_600x800.jpg')
cv.imshow('image ', img)

b,g,r = cv.split(img) # split is a function that is used to split an image into its individual color channels. It takes one argument: the image. The function returns a list of arrays, where each array represents one of the color channels in the image. The order of the color channels in the list is determined by the color space of the image. For example, if the image is in the BGR color space, the first array in the list will represent the blue channel, the second array will represent the green channel, and the third array will represent the red channel.
cv.imshow('blue' , b)
cv.imshow('green ' , g)
cv.imshow('red ' , r)

print(img.shape) # shape is a property of an image that returns a tuple of the dimensions of the image. The first element of the tuple is the height of the image, the second element is the width of the image, and the third element is the number of color channels in the image. For example, if an image has a height of 600 pixels, a width of 800 pixels, and 3 color channels (BGR), the shape property will return (600, 800, 3).
print(b.shape) # shape is a property of an image that returns a tuple of the dimensions of the image. The first element of the tuple is the height of the image, the second element is the width of the image, and the third element is the number of color channels in the image. For example, if an image has a height of 600 pixels, a width of 800 pixels, and 3 color channels (BGR), the shape property will return (600, 800, 3).
print(g.shape) # shape is a property of an image that returns a tuple of the dimensions of the image. The first element of the tuple is the height of the image, the second element is the width of the image, and the third element is the number of color channels in the image. For example, if an image has a height of 600 pixels, a width of 800 pixels, and 3 color channels (BGR), the shape property will return (600, 800, 3).
print(r.shape) # shape is a property of an image that returns a tuple of the dimensions of the image. The first element of the tuple is the height of the image, the second element is the width of the image, and the third element is the number of color channels in the image. For example, if an image has a height of 600 pixels, a width of 800 pixels, and 3 color channels (BGR), the shape property will return (600, 800, 3).

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)

blank = np.zeros(img.shape[:2], dtype = 'uint8') # np.zeros is a function that is used to create an array of zeros. It takes two arguments: the shape of the array and the data type of the array. The shape of the array is specified as a tuple of integers, where each integer represents the size of the corresponding dimension of the array. The data type of the array is specified as a string, where 'uint8' represents an unsigned 8-bit integer.

b,g ,r = cv.split(img)  
blue = cv.merge([b,blank,blank]) # merge is a function that is used to merge multiple arrays into a single array. It takes one argument: a list of arrays. The order of the arrays in the list determines the order of the color channels in the merged array. For example, if the first array in the list represents the blue channel, the second array represents the green channel, and the third array represents the red channel, the merged array will be in the BGR color space.
green = cv.merge([blank,g,blank]) # merge is a function that is used to merge multiple arrays into a single array. It takes one argument: a list of arrays. The order of the arrays in the list determines the order of the color channels in the merged array. For example, if the first array in the list represents the blue channel, the second array represents the green channel, and the third array represents the red channel, the merged array will be in the BGR color space.
red = cv.merge([blank,blank,r]) # merge is a function that is used to   merge multiple arrays into a single array. It takes one argument: a list of arrays. The order of the arrays in the list determines the order of the color channels in the merged array. For example, if the first array in the list represents the blue channel, the second array represents the green channel, and the third array represents the red channel, the merged array will be in the BGR color space.
cv.imshow('blue' , blue)
cv.imshow('green ' , green)
cv.imshow('red ' , red)






cv.waitKey(0)