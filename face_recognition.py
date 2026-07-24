import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# feature = np.load('feature.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'D:\Python\OpenCV\cv photos\val\ben_afflek\2.jpg')

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

cv.imshow('Person' , gray )

# Detect the faces in the image 
face_rect = haar_cascade.detectMultiScale(gray , 1.1 , 4 )

for(x,y,w,h) in face_rect:
    faces_roi = gray[y:y+h , x:x+w]

    label , confidence = face_recognizer.predict(faces_roi)
    print('label confidence ' , label , confidence)
    
    cv.putText(img  , str(people[label]) , (20,20) , cv.FONT_HERSHEY_COMPLEX , 1.0 , (0,255,0) , thickness=2)
    cv.rectangle(img , (x,y) , (x+w ,y+h) , (0 , 255 ,0) , thickness=2)
cv.imshow("Detected Faces" , img)
# cv.imshow('Image', img)
cv.waitKey(0)