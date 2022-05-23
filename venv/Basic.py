import cv2
import numpy as np
import face_recognition

imgOne = face_recognition.load_image_file('imageDB/AmanKhokhar.jpg')
imgOne = cv2.cvtColor(imgOne,cv2.COLOR_BGR2RGB)

imgTwo = face_recognition.load_image_file('imagesTest/IMG_20200306_103633.jpg')
imgTwo = cv2.cvtColor(imgTwo,cv2.COLOR_BGR2RGB)

faceLocMain = face_recognition.face_locations(imgOne)[0]
endFaceMain = face_recognition.face_encodings(imgOne)[0]
cv2.rectangle(imgOne,(faceLocMain[3],faceLocMain[0]),(faceLocMain[1],faceLocMain[2]),(0,255,0),2)

faceLocTest = face_recognition.face_locations(imgTwo)[0]
endFaceTest = face_recognition.face_encodings(imgTwo)[0]

result = face_recognition.compare_faces([endFaceMain],endFaceTest)
face_distances = face_recognition.face_distance([endFaceMain], endFaceTest)
percen = (1-face_distances[0])*100

print(result[0])

if result[0]:
    cv2.rectangle(imgTwo,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(0,255,0),2)
    cv2.putText(imgTwo,str(round(face_distances[0],2)),(faceLocTest[3],faceLocTest[0]-10),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
else:
    cv2.rectangle(imgTwo,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(0,0,255),2)
    cv2.putText(imgTwo, str(round(face_distances[0],2)), (faceLocTest[3], faceLocTest[0] - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255),2)

cv2.imshow('Main',imgOne)
cv2.imshow('Test',imgTwo)
cv2.waitKey(0)