import csv
import os
from datetime import datetime

# Directory to save attendance records
ATTENDANCE_DIR = "Attendance"

def save_attendance(student_id, student_name):
    # Ensure the directory exists
    if not os.path.exists(ATTENDANCE_DIR):
        os.makedirs(ATTENDANCE_DIR)

    # Create a file for today's attendance
    date_str = datetime.now().strftime("%Y-%m-%d")
    attendance_file = os.path.join(ATTENDANCE_DIR, f"Attendance_{date_str}.csv")

    # Check if the file exists
    file_exists = os.path.isfile(attendance_file)

    # Open the file in append mode
    with open(attendance_file, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Write the header row if the file is being created for the first time
        if not file_exists:
            writer.writerow(["Student ID", "Name", "Date", "Time", "Status"])

        # Record the attendance
        time_str = datetime.now().strftime("%H:%M:%S")
        writer.writerow([student_id, student_name, date_str, time_str, "Present"])
        print(f"Attendance marked for {student_name} ({student_id}) at {time_str}.")

# Example usage
if __name__ == "__main__":
    while True:
        student_id = input("Enter Student ID (or type 'exit' to stop): ").strip()
        if student_id.lower() == "exit":
            break

        student_name = input("Enter Student Name: ").strip()
        save_attendance(student_id, student_name)
