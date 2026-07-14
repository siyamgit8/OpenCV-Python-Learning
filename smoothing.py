import cv2  as cv 
img = cv.imread('cv photos/img_600x800.jpg')
cv.imshow('image' , img)

#Avereging
avg = cv.blur(img  ,(3,3)) # this function takes two arguments, first is the image and second is the kernel size. The kernel size should be odd and positive.
cv.imshow('average blur ' , avg )
# the kernel size is the size of the filter that is used to smooth the image. The larger the kernel size, the more the image will be blurred.

# Gaussian Blur 
gauss = cv.GaussianBlur(img , (3,3) , 0) # this function takes three arguments, first is the image, second is the kernel size and third is the standard deviation. The kernel size should be odd and positive. The standard deviation is used to control the amount of blur. The larger the standard deviation, the more the image will be blurred.
cv.imshow('Gaussian blur ' , gauss ) # the kernal size cannot be even and the standard deviation cannot be negative because it will not make sense. The standard deviation is used to control the amount of blur. The larger the standard deviation, the more the image will be blurred.

# Median Blur 
# more effecting in removing salt and pepper noise.
median = cv.medianBlur(img , 3) # this function takes two arguments, first is the image and second is the kernel size. The kernel size should be odd and positive. The median blur is more effective in removing salt and pepper noise because it replaces each pixel value with the median value of the neighboring pixels.
cv.imshow('Median blur ' , median ) # the kernel size cannot be even because it will not make sense. The median blur is more effective in removing salt and pepper noise because it replaces each pixel value with the median value of the neighboring pixels.  

# Bilateral blurring 
bilateral = cv.bilateralFilter(img , 5 , 15 , 15 )
cv.imshow('Bilateral blur ' , bilateral ) # this function takes four arguments, first is the image, second is the diameter of the pixel neighborhood, third is the standard deviation in color space and fourth is the standard deviation in coordinate space. The larger the diameter, the more the image will be blurred. The larger the standard deviation in color space, the more the image will be blurred. The larger the standard deviation in coordinate space, the more the image will be blurred.

cv.waitKey(0) 

# the difference between the four types of blurring is that the average blur and Gaussian blur are linear filters, while the median blur and bilateral blur are non-linear filters. The average blur and Gaussian blur are more effective in removing Gaussian noise, while the median blur and bilateral blur are more effective in removing salt and pepper noise. The average blur and Gaussian blur are more effective in preserving edges, while the median blur and bilateral blur are more effective in preserving edges. The average blur and Gaussian blur are more effective in preserving details, while the median blur and bilateral blur are more effective in preserving details.