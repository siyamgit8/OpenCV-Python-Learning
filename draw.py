import cv2 as cv
import numpy as np 

blank = np.zeros((500, 500 , 3  ), dtype='uint8') ## creating a blank image of 500x500 pixels     ## first argument is width and second argument is height and third argument is color channels (3 for RGB and 1 for grayscale)
cv.imshow('blank' , blank)

# 1 painting the image with a color 
blank[200:300 , 300:400] = 0,255,0 ## painting the image with a color (BGR format)  ## first argument is blue, second argument is green and third argument is red
cv.imshow('green ' , blank)

# 2. draw a rectangle 
cv.rectangle(blank , (0,0) , (250,250) , (0,255,0) , thickness=2) ## drawing a rectangle on the image  ## first argument is the image, second argument is the top left corner of the rectangle, third argument is the bottom right corner of the rectangle, fourth argument is the color of the rectangle (BGR format), fifth argument is the thickness of the rectangle
cv.imshow('rectangle' , blank) ## midpoint can be calculated by : blank.shape[0]//2 , blank.shape[1]//2

# 3. draw a circle
cv.circle(blank , (250,250) , 250 , (0,0,255) , thickness=2) ## drawing a circle on the image  ## first argument is the image, second argument is the center of the circle, third argument is the radius of the circle, fourth argument is the color of the circle (BGR format), fifth argument is the thickness of the circle
cv.imshow('circle' , blank)

# 4. draw a line
cv.line(blank , (500,500) , (250,250) , (255,255,255) , thickness=3) ## drawing a line on the image  ## first argument is the image, second argument is the starting point of the line, third argument is the ending point of the line, fourth argument is the color of the line (BGR format), fifth argument is the thickness of the line
cv.imshow('line' , blank)

# 5. write text on the image
cv.putText(blank , 'Hello My Love suggi ' , (100,225) , cv.FONT_HERSHEY_TRIPLEX , 1.0 , (0,255,0) , 2) ## writing text on the image  ## first argument is the image, second argument is the text to be written, third argument is the bottom left corner of the text, fourth argument is the font of the text, fifth argument is the font scale, sixth argument is the color of the text (BGR format), seventh argument is the thickness of the text
cv.imshow('tezt' , blank)
cv.waitKey(0)