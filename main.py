import cv2

cap = cv2.VideoCapture(0)
#def tracker():
#trackeer
tracker = cv2.TrackerMOSSE_create()
success, img = cap.read()
bbox = cv2.selectROI("tracking",img,False)
tracker.init(img,bbox)

def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"TRACKING",(25,25),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,0.7,(0,255,0),3)




while True:
    timer = cv2.getTickCount()
    success,img = cap.read()
    success,bbox= tracker.update(img)

    if success:
        drawBox(img,bbox)


    else:
        cv2.putText(img, "LOST", (50,50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.7, (0, 0, 255), 3)

    #fps cal

    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img,str(int(fps)),(25,25),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,0.7,(0,0,255),3)




    cv2.imshow("TRACKING",img)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break