import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow('SAM')
image_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print('failed to grab image')
        break

    cv2.imshow('SAM',frame)

    k = cv2.waitKey(1)

    if k%256 == 27:
        print("Escape hit, closing the app")
        break

    elif k%256 == 32:
        image_name = "opencv_frame_{}.jpg".format(image_counter)
        cv2.imwrite(image_name, frame)
        print('Image taken')
        image_counter+=1
cam.release()
cv2.destroyAllWindows()