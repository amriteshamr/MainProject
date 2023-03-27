import face_recognition
from PIL import Image, ImageDraw
from Face_Rec import FaceRec
import pickle

#creates an instance of thr Face_Rec class called fr
fr = FaceRec()

#final list contains the names of the identified people in the image
final = []

#tolerance refers to the threshold or acceptable limit for matching faces 
TOLERANCE = 0.5

#this directory is used to store the faces pulled from each image
pulledfaces_dir = 'Pulled Faces/'

#loads the data files which containts the encodings and names of the known faces
with open('dataset_faces.dat', 'rb') as f:
	known_encod = pickle.load(f)

with open('dataset_names.dat', 'rb') as f:
	known_names = pickle.load(f)

#known_encod, known_names = fr.load_images("Training_images/")
# test = 'Test_images/test_image2.jpg'

#Capture method loads camera and allows us to click a picture by pressing the space key. It returns the clicked image's name
#test = []
test = fr.capture()

faces_in_image = []
#for i in range(3):
    #faces_in_image = fr.pullfaces(test[i])
faces_in_image = fr.pullfaces(test)

#final = fr.identifyfromfolder(pulledfaces_dir, known_encod, known_names, TOLERANCE)

#Identify method returns the face locations and encodings of all the faces in the clicked image
test_locations, test_encodings = fr.identify(test)
img = face_recognition.load_image_file(test)
pil_image = Image.fromarray(img)

draw = ImageDraw.Draw(pil_image)

for(top, right, bottom, left), face_encoding in zip(test_locations, test_encodings):
    matches = face_recognition.compare_faces(known_encod, face_encoding, TOLERANCE)

    name = "Unknown"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_names[first_match_index]
        final.append(name)
    
    draw.rectangle(((left, top), (right, bottom)), outline=(255,255,255))
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

print(final)
pil_image.show()
pil_image.save('Results/test.jpg')