import cv2
import numpy as np
###################################################
frame_width = 640
frame_height = 480
nplatecascade = cv2.CascadeClassifier("Resources/haarcascade_licence_plate_rus_16stages.xml")
minArea = 200
colour = (255,0,255)
###################################################

cap = cv2.VideoCapture(0)
cap.set(3,frame_width)
cap.set(4,frame_height)
cap.set(10,150)
while True:
    sucess,img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberPlate = nplatecascade.detectMultiScale(imgGray, 1.1, 4)


    for (x,y,w,h) in numberPlate:
        area = w*h
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
        cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,colour,2)
        imgroi = img[y:y+h,x:x+w]
        cv2.imshow("ROI",imgroi)
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



