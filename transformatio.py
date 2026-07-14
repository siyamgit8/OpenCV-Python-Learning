import cv2 as cv
import numpy as np 
img = cv.imread('cv photos/mountain.jpg')


cv.imshow('image ' , img)

# translation
def translate(img, x , y ): # x and y are the number of the pixels you would shift 
    tansMAt = np.float32([[1,0,x] ,[0,1,y]]) # translation matrix is a 2x3 matrix that is used to shift an image in the x and y direction
    dimensions = (img.shape[1] , img.shape[0])
    return cv.warpAffine(img , tansMAt , dimensions) # warpAffine is a function that is used to apply an affine transformation to an image. It takes three arguments: the image, the transformation matrix, and the dimensions of the output image.
    # -x --> left
    # -y --> up 
    # x --> right 
    # y --> down 

translated = translate(img , 100 , 100)
cv.imshow('translated ' , translated)

# rotate 

def rotate(img , angle  , rotpoint = None):
    (height , width ) = img.shape[:2] # img.shape returns a tuple of the dimensions of the image. The first element is the height, the second element is the width, and the third element is the number of channels (if the image is in color). The [:2] slice is used to get only the height and width.
    if rotpoint is None:
        rotpoint = (width//2 , height//2) # if the rotation point is not specified, the image will be rotated around its center 
    rotMat = cv.getRotationMatrix2D(rotpoint , angle , 1.0)
    dimensions = (width , height)

    return cv.warpAffine(img , rotMat , dimensions) # warpAffine is a function that is used to apply an affine transformation to an image. It takes three arguments: the image, the transformation matrix, and the dimensions of the output image.
rotated  = rotate(img , 45 )
cv.imshow('rotated ' , rotated)

# Resizing

resized = cv.resize(img , (500 , 500) , interpolation = cv.INTER_CUBIC) # resize is a function that is used to resize an image. It takes three arguments: the image, the dimensions of the output image, and the interpolation method. The interpolation method is used to determine how the pixels in the output image are calculated from the pixels in the input image. The INTER_CUBIC method is used to calculate the pixels in the output image using a cubic convolution algorithm.
cv.imshow('resized ' , resized)

# flipping

flipped = cv.flip(img , -1) # flip is a function that is used to flip an image. It takes two arguments: the image and the flip code. The flip code is used to determine how the image is flipped. A flip code of 0 flips the image vertically, a flip code of 1 flips the image horizontally, and a flip code of -1 flips the image both vertically and horizontally.
cv.imshow('flipped ' , flipped)

# cropping
 
cropped = img[200:400 , 300:400] # cropping is a process of extracting a portion of an image. It is done by specifying the coordinates of the top-left and bottom-right corners of the rectangle that defines the portion of the image to be extracted. The coordinates are specified in the format [y1:y2 , x1:x2], where y1 and y2 are the y-coordinates of the top-left and bottom-right corners, and x1 and x2 are the x-coordinates of the top-left and bottom-right corners.
cv.imshow('cropped ' , cropped)
cv.waitKey(0)



