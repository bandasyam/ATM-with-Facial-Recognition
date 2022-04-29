from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import cv2
import face_recognition
import os
import numpy as np

# In face recognition :
# We need a image
# We need to encode it (for that 1st we have to BGR img to RGB img)
# Then we can either match that face with other or any other things

list = []
var = ""

def everything():
    path = 'images'
    images = []
    onlyNames = []
    myImagesList = os.listdir(path)  # displays all the files in that path as a list
    global successValue

    for i in myImagesList:
        curimg = cv2.imread(path + "/" + i)
        images.append(curimg)  # Now all the images in folder are stored in list named images
        onlyNames.append(os.path.splitext(i)[0])
    print(onlyNames)

    def encodingImages(images):
        encodedImagesList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodedImagesList.append(encode)
        return encodedImagesList

    encodedlistKnown = encodingImages(images)
    print('Encoding complete .....')

    # Upto here we have images and we encoded it Therefore
    # We have encoded images now we need images to find a match that comes from live opencv webcam

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("ICFAI BANK")
    while True:
        success, frame = cam.read()
        # now we are reducing the image size because it helps in speeding up the process
        # imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        # Now we got encodings from live webcam
        # Now we are going to match live webcam faces encoded with our stored encoded images

        global list
        global var
        # list = []
        # var = ""
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodedlistKnown, encodeFace)
            # faceDis = face_recognition.face_distance(encodedlistKnown, encodeFace)
            if not list:
                list.append(matches)
            print(matches)
            if True in matches:
                if not var:
                    var = var + "success"
            # matchIndex = np.argmin(faceDis)
            # if matches[matchIndex]:
            #     name = onlyNames[matchIndex].upper()
            #     print(name)
        print(var)
        print(list)
        cv2.imshow("Webcam", frame)
        k = cv2.waitKey(1)
        if k % 256 == 27:  # Here from ASCII this is escape key so pressing escape key
            print("Escape hit, closing window")
            break
        if True in list[0]:
            print("Mega success")

    cam.release()
    cv2.destroyAllWindows()



# everything()