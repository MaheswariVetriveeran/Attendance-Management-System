import cv2
import os

def capture_images():
    cam = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    count = 0
    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            count += 1
            cv2.imwrite(f"TrainingImage/{id}_{count}.jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow("Capture Images", frame)
        if cv2.waitKey(100) & 0xFF == 27 or count >= 20:
            break

    cam.release()
    cv2.destroyAllWindows()
    print("Images captured successfully!")

if __name__ == "__main__":
    capture_images()
