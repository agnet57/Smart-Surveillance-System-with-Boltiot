#Program to Detect the Face and Recognise the Person based on the data from face-trainner.yml

import cv2 #For Image processing 
import numpy as np #For converting Images to Numerical array 
import os #To handle directories 
from PIL import Image #Pillow lib for handling images 
def recog(a):
    #labels = ["srikant", "intruder","Elon Musk"] 
    labels=["pritam","elon"]
    #face_cascade = cv2.CascadeClassifier('F:/bolt iot security project/face recg harcascades/haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("F:/bolt iot security project/face recg harcascades/face-trainner.yml")

    cap = cv2.VideoCapture(1) #Get vidoe feed from the Camera

    while(a):

        ret, img = cap.read() # Break video into frames 
        gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert Video frame to Greyscale
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5) #Recog. faces
        #faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w] #Convert Face to greyscale 

            id_, conf = recognizer.predict(roi_gray) #recognize the Face
            print(id_)
            if conf>=80:
                    font = cv2.FONT_HERSHEY_SIMPLEX #Font style for the name 
                    name = labels[id_] #Get the name from the List using ID number
                    if id_==1:
                        return 1
                        break
                    cv2.putText(img, name, (x,y), font, 1, (0,0,255), 2)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('Preview',img) #Display the Video
     
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
#recog(True)

  