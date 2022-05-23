import cv2
import numpy as np
import face_recognition
import  os

path = 'imageDB'
images = []
imageNames =[]
tmpList = os.listdir(path)

for imgname in tmpList:
    curImg = cv2.imread(f'{path}/{imgname}')
    images.append(curImg)
    imageNames.append(os.path.splitext(imgname)[0])

print('Starting image encoding for known people....')
def findEncodings(images):
    encodingList = []
    i = 1
    file = open("encodes.txt", "a")
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodingList.append(encode)
    np.savetxt("encodes.txt", encodingList)
    return encodingList

knownEncodingList = findEncodings(images)
print('Encoding Complete....')
print('Starting Camera')

cap = cv2.VideoCapture(0)
counter = 9
matchIndex = -1
matches = []
faceDis = None
while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    counter+=1
    if counter % 10 == 0:
        facesLocCurImg = face_recognition.face_locations(imgS)
        encodesCurImg = face_recognition.face_encodings(imgS, facesLocCurImg)
        for encode,faceLoc in zip(encodesCurImg,facesLocCurImg):
            matches = face_recognition.compare_faces(knownEncodingList,encode)
            faceDis = face_recognition.face_distance(knownEncodingList,encode)
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex] == True:
                name = imageNames[matchIndex] + ' | ' + str(round((1-faceDis[matchIndex])*100,2)) + '%'
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4

                cv2.rectangle(img,(x1,y1),(x2,y2), (0, 255, 0), 2)
                cv2.putText(img,name,(x1,y1-10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        if not facesLocCurImg:
            matchIndex = -1
    else:
        try:
            if matches[matchIndex] == True:
                name = imageNames[matchIndex] + ' | ' + str(round((1 - faceDis[matchIndex]) * 100, 2)) + '%'
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, name, (x1, y1 - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        except Exception:
            pass
    if counter == 100:
        counter = 1

    cv2.imshow('Webcam',img)
    cv2.waitKey(1)