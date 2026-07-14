import cv2 as cv 
img = cv.imread('cv photos/Screenshot 2026-05-07 023908.png')
cv.imshow('Siyam ' , img)

# converting to the greyscale

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('GRay' , gray)

# how to blur an image 
blur = cv.GaussianBlur(img , (7,7) , cv.BORDER_DEFAULT)
cv.imshow('blur' ,blur)

# edge cascade 
canny = cv.Canny(img, 125 , 175) # if we pass the blur of the image the edge detection will be desriable
cv.imshow('canny' , canny)

# dilating image
dilated = cv.dilate(canny , (3,3) , iterations = 1)
cv.imshow('dilated' , dilated)

# eroding 
eroded = cv.erode(dilated  , (3,3) , iterations = 1)
cv.imshow('eroded ' , eroded )

# resize 
resized = cv.resize(img ,(500,500) ,interpolation=cv.INTER_AREA )
cv.imshow('resize' , resized)

# cropping
cropped = img[50:100 , 200:400]
cv.imshow('cropped' , cropped)





cv.waitKey(0)
