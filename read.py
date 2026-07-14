 
import cv2 as cv
## reading images:

# img = cv.imread('cv photos/IMG_20251108_152604.jpg')

# cv.imshow('Siyam', img)

# cv.waitKey(0)
## not required to use cv2.destroyAllWindows() in jupyter notebook





# reading videos

capture = cv.VideoCapture('cv videos/video1.mp4')

while True:
    istrue, frame = capture.read() ## returns a boolean value and the frame 
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'): ## wait for 20 milliseconds and if d is pressed then break the loop
        break
capture.release() ## release the video capture object
cv.destroyAllWindows() ## destroy all the windows

