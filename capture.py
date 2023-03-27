import cv2

cam = cv2.VideoCapture(0)

#cv2.namedWindow("Attendance Marker")

img_counter = 0

while True:
    ret,frame = cam.read()
    
    if not ret:
        print("failed to grab frame")
        break
    
    cv2.imshow("test", frame)
    
    k = cv2.waitKey(1)
    
    if k == 27:
        break
    elif k ==32:
        img_name = "Attendane_CS7_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("Image taken")
        img_counter+=1


cam.release()
cv2.destroyAllWindows()