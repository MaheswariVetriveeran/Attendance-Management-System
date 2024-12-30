import cv2

def recognize_faces():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("TrainingImageLabel/trained_model.yml")
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
            name = f"ID: {id}" if confidence < 50 else "Unknown"
            cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)
        cv2.imshow("Attendance", frame)
        if cv2.waitKey(10) == 27:  # Press 'ESC' to exit
            break
    cam.release()
    cv2.destroyAllWindows()
