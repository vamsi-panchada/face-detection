import streamlit as st
import cv2

st.title('Face Detection using WebCam')
run = st.button('RUN')
stop = st.button('STOP')
if run:
    # stop = False
    Frame_Window = st.image([])
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
        if stop:
            print('hitting point 1')
            run = False
            cam.release()
            Frame_Window = st.empty()
    if stop:
        print('hitting point 2')
        run = False
        cam.release()
        Frame_Window = st.empty()
    cam.release()