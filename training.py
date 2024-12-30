import os
import cv2
import numpy as np

# Function to get images and labels from the 'TrainingImage' directory
def get_images_and_labels(training_image_folder):
    faces = []
    labels = []
    student_ids = {}  # A dictionary to map student IDs (strings) to integers
    id_counter = 0
    
    # Traverse through the TrainingImage folder
    for folder_name in os.listdir(training_image_folder):
        folder_path = os.path.join(training_image_folder, folder_name)
        
        # Process only if it's a directory
        if os.path.isdir(folder_path):
            # Map each folder_name (student ID) to a unique integer
            if folder_name not in student_ids:
                student_ids[folder_name] = id_counter
                id_counter += 1
            
            for filename in os.listdir(folder_path):
                img_path = os.path.join(folder_path, filename)
                
                # Ensure the file is an image (jpg or png)
                if filename.endswith('.jpg') or filename.endswith('.png'):
                    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # Convert image to grayscale
                    
                    # Append image data and corresponding integer label
                    faces.append(img)
                    labels.append(student_ids[folder_name])  # Use the integer ID for labeling
                    
    return faces, labels

# Function to train the model
def train_model():
    # Define the folder where images are stored
    training_image_folder = "TrainingImage"
    # Define the path where the trained model will be saved
    trained_model_file = "TrainingImageLabel/trained_model.yml"
    
    print("Training the model...")
    
    # Get images and labels
    faces, labels = get_images_and_labels(training_image_folder)
    
    if len(faces) == 0:
        print("No training images found!")
        return
    
    # Initialize the LBPH face recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    
    # Train the model using the images and labels
    recognizer.train(faces, np.array(labels))
    
    # Save the trained model to a file
    recognizer.save(trained_model_file)
    print(f"Model trained and saved as {trained_model_file}")
    
if __name__ == '__main__':
    train_model()
