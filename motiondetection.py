import cv2


accesscamera = cv2.VideoCapture(0)
check, frame1 = accesscamera.read()
check, frame2 = accesscamera.read()


while accesscamera.isOpened():

    #print(frame3)
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=1)
    # edges = cv2.Canny(gray,30,200)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for contour in contours:
        (x,y,w,h)  = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 9000:
            cv2.putText(frame1, "Status:{}".format('NO MOVEMENT RECOGNISED'), (10, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                        (0, 255,0 ), 3)

            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),1)
        cv2.putText(frame1,"Status:{}".format('Movement'),(10,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),3)


    #print(frame4)
    cv2.imshow("online feed",frame1)
    frame1 = frame2
    check,frame2 = accesscamera.read()
    if ord('q') == cv2.waitKey(20):
        break
accesscamera.release()
cv2.destroyAllWindows()
