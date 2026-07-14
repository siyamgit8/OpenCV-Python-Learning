import cv2 as cv

img = cv.imread('cv photos/IMG_20251108_152604.jpg')
cv.imshow('Siyam', img)

def rescaleFrame(frame, scale=0.75):
    # this method works for images, videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
def changeres(width , height):
    # this method works for live video only
    capture.set(3,width)
    capture.set(4,height)

# reading new images and videos and rescaling them
resized_image = rescaleFrame(img)
cv.imshow('image' , resized_image)
capture = cv.VideoCapture('cv videos/video1.mp4')

while True:
    istrue, frame = capture.read() ## returns a boolean value and the frame 
    frame_resized  = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'): ## wait for 20 milliseconds and if d is pressed then break the loop
        break
capture.release() ## release the video capture object
cv.destroyAllWindows() ## destroy all the windows


cv.waitKey(0)
