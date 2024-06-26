import json
import os
import sys

# Define the URLs
base = "https://ums.paruluniversity.ac.in/"
login = "https://ums.paruluniversity.ac.in/Login.aspx"
dashboard = "https://ums.paruluniversity.ac.in/StudentPanel/StudentDashboard.aspx"
attendence = "https://ums.paruluniversity.ac.in/StudentPanel/TTM_Attendance/TTM_Attendance_StudentAttendance.aspx"

# Path to the config file
config_file_path = 'config.json'

# Check if the config file exists
if not os.path.isfile(config_file_path):
    print("Error: config file is not configured")
    sys.exit(1)

# Read the config file
with open(config_file_path, 'r') as file:
    try:
        config = json.load(file)
    except json.JSONDecodeError:
        print("Error: config file is not properly formatted")
        sys.exit(1)

# Get email and password from the config
email = config.get('email')
password = config.get('password')

# Check if email and password are present
if not email or not password:
    print("Error: config file is missing email or password")
    sys.exit(1)

# Print the read values (for debugging purposes)
print(f"Email: {email}")
print(f"Password: {password}")

# Your further code goes here
