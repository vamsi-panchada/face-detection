import streamlit as st
import cv2

st.title('Face Detection using WebCam')
run = st.button('RUN')
Frame_Window = st.image([])
stop = st.button('STOP')
if run:
    cam = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('face.xml')
    while run:
        res, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        Frame_Window.image(frame)
    cam.release()