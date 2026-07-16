import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

img = cv.imread('cv photos/teddy.jpg')


gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)

#GRayscale histogram 

# gray_hist = cv.calcHist([gray] , [0] , None , [256] , [0,255]) # this function 

# plt.figure()
# plt.title('grayscale histogram')
# plt.xlabel('bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0 ,256])
# plt.show()


# Color Histogram 
plt.figure()
plt.title('color histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
colors = ('b' , 'g' , 'r')
for i , col in enumerate(colors):
    hist = cv.calcHist([img] , [i] , None , [256] , [0 ,256]) # this function used to 
    plt.plot(hist , color = col)
    plt.xlim([0 ,256])
plt.show()


# cv.imshow('Image', img)
cv.waitKey(0)