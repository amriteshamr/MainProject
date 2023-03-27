import face_recognition
import cv2
import os
import glob
import numpy as np
from PIL import Image, ImageDraw

class FaceRec:
    def __init__(self):
        self.known_faceencodings = []
        self.known_facenames = []
    
    '''def load_images(self, images_path):
        
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} encoding images found.".format(len(images_path)))

        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename only from the initial file path.
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Get encoding
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Store file name and file encoding
            self.known_faceencodings.append(img_encoding)
            self.known_facenames.append(filename)
            
        print("Encoding images loaded")
        return self.known_faceencodings, self.known_facenames'''

   #Identify method gets the clicked image as parameter and returns the face locations and encodings of all the faces in it
    
    def identify(self,test_image):
        test = face_recognition.load_image_file(test_image)
        face_locations = face_recognition.face_locations(test)
        face_encodings = face_recognition.face_encodings(test, face_locations)

        return face_locations, face_encodings 



    #Capture method loads camera and allows us to click a picture by pressing the space key. It returns the clicked image's name
    def capture(self):
        cam = cv2.VideoCapture(2)
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
                #time_interval = 3
                #images = []
                #for i in range(3):
                    #time.sleep(time_interval)
                    #image_name = "clicked_image_{}.jpg".format(image_counter)
                    #cv2.imwrite(image_name, frame)
                    #print('Image taken')
                    #image_counter+=1
                    #images.append(image_name)
                #return images

                image_name = "opencv_frame_{}.jpg".format(image_counter)
                cv2.imwrite(image_name, frame)
                print('Image taken')
                image_counter+=1
                return image_name            
            
                
        cam.release()
        cv2.destroyAllWindows()
    
    def pullfaces(self, getfaceimg):
        pulled_faces =[]
        image = face_recognition.load_image_file(getfaceimg)
        face_locations = face_recognition.face_locations(image)

        for face_location in face_locations:
            top, right, bottom, left = face_location
            face_img = image[top - 40 :bottom + 20, left - 20:right + 20]
            pil_image = Image.fromarray(face_img)
            pil_image.save(f'Pulled Faces/{face_location}.jpg')
            pulled_faces.append(face_img)
            return pulled_faces

    '''def identifyfromfolder(self, path, kencod, knames, tol):
        present = []
        for img in path:
            pic = face_recognition.load_image_file(img)
            faceloc = face_recognition.face_imglocations(pic)
            faceenc = face_recognition.face_encodings(pic, faceloc)

            for (top, left, bottom, right), faceencods in zip(faceloc, faceenc):
                match = face_recognition.compare_faces(kencod, faceencods, tol)

                name = 'Unknown'

                if True in match:
                    firstmtchindx = match.index(True)
                    name = knames[firstmtchindx]
                    present.append(name)

        return present'''