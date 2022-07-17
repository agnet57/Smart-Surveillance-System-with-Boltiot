import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(1)
# To use a video file as input 
#cap = cv2.VideoCapture('filename.mp4')

def pr():
    while True:
        # Read the frame
        _, img = cap.read()
    
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        name=["intruder"]
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, name[0], (x,y), font, 1, (0,0,255), 2)
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
        # Display
        cv2.imshow('img', img)
    
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
            
    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()
#pr()    