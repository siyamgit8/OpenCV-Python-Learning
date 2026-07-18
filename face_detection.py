import cv2 as cv

import numpy as np

img = cv.imread('cv photos/women.png')

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml') # really sensitive to noise thats why they recongnise mismatch faces when they are more number in the faces in the image 

faces_rect = haar_cascade.detectMultiScale(gray , scaleFactor=1.1  , minNeighbors=7) # 
print('nunber of faces ' , len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img , (x,y) , (x+w , y+h) , (0 ,255 ,0) , thickness=3 )
cv.imshow('detected faces' , img)


cv.imshow('gray' , gray)

# cv.imshow('group', img)

cv.waitKey(0)