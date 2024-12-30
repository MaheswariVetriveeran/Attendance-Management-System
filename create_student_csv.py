import csv
import os

# File path for the student details CSV
CSV_FILE = "StudentDetails/StudentDetails.csv"

def create_or_update_student_csv():
    # Ensure the directory exists
    if not os.path.exists("StudentDetails"):
        os.makedirs("StudentDetails")

    # Check if the CSV file exists
    file_exists = os.path.isfile(CSV_FILE)

    # Open the CSV file in append mode
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Write the header row if the file is being created for the first time
        if not file_exists:
            writer.writerow(["Enrollment Number", "Name"])

        # Input student details
        while True:
            enrollment_no = input("Enter Enrollment Number (or type 'exit' to stop): ").strip()
            if enrollment_no.lower() == "exit":
                break

            name = input("Enter Student Name: ").strip()

            # Check if the enrollment number already exists in the file
            if is_enrollment_exists(enrollment_no):
                print(f"Enrollment Number {enrollment_no} already exists. Try again.")
            else:
                # Add the student details to the CSV file
                writer.writerow([enrollment_no, name])
                print(f"Student {name} with Enrollment Number {enrollment_no} added successfully!")

def is_enrollment_exists(enrollment_no):
    # Check if the enrollment number already exists in the CSV file
    if os.path.isfile(CSV_FILE):
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                if row[0] == enrollment_no:
                    return True
    return False

if __name__ == "__main__":
    create_or_update_student_csv()

