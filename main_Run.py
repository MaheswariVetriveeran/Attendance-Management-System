import tkinter as tk
from tkinter import messagebox
import os
import training
import testing

def main_app():
    root = tk.Tk()
    root.title("Attendance Management System")
    root.geometry("500x400")

    def capture_images():
        os.system("python mini_app.py")

    def train_faces():
        training.train_model()

    def recognize_faces():
        testing.recognize_faces()

    tk.Button(root, text="Capture Images", command=capture_images).pack(pady=20)
    tk.Button(root, text="Train Images", command=train_faces).pack(pady=20)
    tk.Button(root, text="Automatic Attendance", command=recognize_faces).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_app()
