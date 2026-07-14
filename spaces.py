import cv2 as cv 
import matplotlib.pyplot as plt


img = cv.imread('cv photos/img_600x800.jpg')
cv.imshow('image' , img)

plt.imshow(img)
plt.show() # displays image as RGB instead of BGR

# BGR to GRAY
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY) # cvtColor is a function that is used to convert an image from one color space to another. It takes two arguments: the image and the color conversion code. The color conversion code is used to determine how the colors in the image are converted from one color space to another. The COLOR_BGR2GRAY color conversion code is used to convert an image from the BGR color space to the GRAY color space.
cv.imshow('gray' , gray)

# BGR TO HSV HUE SATURATION VALUE
hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV) # cvtColor is a function that is used to convert an image from one color space to another. It takes two arguments: the image and the color conversion code. The color conversion code is used to determine how the colors in the image are converted from one color space to another. The COLOR_BGR2HSV color conversion code is used to convert an image from the BGR color space to the HSV color space.
cv.imshow('hsv' , hsv)

# BGR to L*A*B
lab = cv.cvtColor(img , cv.COLOR_BGR2LAB) # cvtColor is a function that is used to convert an image from one color space to another. It takes two arguments: the image and the color conversion code. The color conversion code is used to determine how the colors in the image are converted from one color space to another. The COLOR_BGR2LAB color conversion code is used to convert an image from the BGR color space to the LAB color space.
cv.imshow('lab' , lab) 


# BGR TO RGB 
rgb = cv.cvtColor(img , cv.COLOR_BGR2RGB) # cvtColor is a function that is used to convert an image from one color space to another. It takes two arguments: the image and the color conversion code. The color conversion code is used to determine how the colors in the image are converted from one color space to another. The COLOR_BGR2RGB color conversion code is used to convert an image from the BGR color space to the RGB color space.
cv.imshow('rgb' , rgb)

plt.imshow(rgb)
plt.show() # displays image as RGB instead of BGR

# INVERSE OF IMGAGE 
# We cannot convert an image from one color space to another and then convert it back to the original color space. This is because the conversion process is not reversible. For example, if we convert an image from BGR to GRAY and then convert it back to BGR, we will not get the original image back. This is because the conversion from BGR to GRAY loses information about the color of the image. Therefore, we cannot convert an image from one color space to another and then convert it back to the original color space.

# HSV TO BGR 
hsv_bgr = cv.cvtColor(hsv , cv.COLOR_HSV2BGR) # cvtColor is a function that is used to convert an image from one color space to another. It takes two arguments: the image and the color conversion code. The color conversion code is used to determine how the colors in the image are converted from one color space to another. The COLOR_HSV2BGR color conversion code is used to convert an image from the HSV color space to the BGR color space.
cv.imshow('hsv_bgr' , hsv_bgr)


# lab to bgr
lab_bgr = cv.cvtColor(lab , cv.COLOR_LAB2BGR) # cvtColor is a function that is used to convert an image from one color space to another. It takes two arguments: the image and the color conversion code. The color conversion code is used to determine how the colors in the image are converted from one color space to another. The COLOR_LAB2BGR color conversion code is used to convert an image from the LAB color space to the BGR color space.
cv.imshow('lab_bgr' , lab_bgr)


cv.waitKey(0)
