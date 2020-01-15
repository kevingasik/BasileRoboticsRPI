import numpy as np
import cv2
faceCascade = cv2.CascadeClassifier('/usr/local/lib/python3.7/dist-packages/cv2/data/haarcascade_frontalface_default.xml')
#faceCascade = cv2.CascadeClassifier('lbp_cascade_frontalface.xml')
#eyeCascade= cv2.CascadeClassifier('/usr/local/lib/python3.7/dist-packages/cv2/data/haarcascade_eye.xml')
#faceCascade = cv2.CascadeClassifier('/usr/local/lib/python3.7/dist-packages/cv2/data/haarcascade_fullbody.xml')


cap = cv2.VideoCapture(0)
cap.set(3,1280) # set Width
cap.set(4,730) # set Height
#cv2.namedWindow("output",cv2.WINDOW_NORMAL)

while True:
    ret, img = cap.read()
    #img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=4,     
        minSize=(40, 40)
    )
   


    #faces.append(faces2)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w] 
        #for(ex,ey,ew,eh) in eyes:
        #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
    #image = cv2.imread('img')
    #cv2.resizeWindow("output",(640,480))
    cv2.imshow('video',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
