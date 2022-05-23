import cv2
import mtcnn
import numpy as np
detector = mtcnn.MTCNN()
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    faces = detector.detect_faces(img)
    cv2.imshow('Webcam', img)
    cv2.waitKey(1)





