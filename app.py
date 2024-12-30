import streamlit as st
import pandas as pd

# Title for the web app
st.title('Attendance Management System')

# Display a message
st.write("This is a simple app to view the attendance records.")

# Load the attendance data from CSV
try:
    attendance_data = pd.read_csv('Attendance/attendance.csv')
except FileNotFoundError:
    st.write("No attendance records found. Please make sure the 'attendance.csv' file exists.")
    attendance_data = pd.DataFrame(columns=['Student ID', 'Student Name', 'Status', 'Timestamp'])

# Display the data
if not attendance_data.empty:
    st.dataframe(attendance_data)  # Show the table of attendance data
else:
    st.write("No records to display.")

# Option to filter attendance by student ID or name
st.subheader("Filter Attendance Records")
student_id = st.text_input("Enter Student ID to search", "")
if student_id:
    filtered_data = attendance_data[attendance_data['Student ID'].str.contains(student_id)]
    st.dataframe(filtered_data)