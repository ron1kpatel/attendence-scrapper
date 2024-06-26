import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Enable debugging

# Email Configuration
sender_email = "rp240267@gmail.com" # Enter your email
sender_password = "emim wnkp kdet cnwq"  # Replace with the generated App Password

subject = "Daily Attendance Report"

def sendMail(std):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = std["email"]
    message["Subject"] = subject
    print(std['email'])
    body = f"""
        Hello, {std['name']}.

        Your Attendance Report 
        Percentage = {std['attendance']['percentage']}
        ----------------------------
        Total Slots = {std['attendance']['total_slots']}
        Present = {std['attendance']['present_slots']}
        Absent = {std['attendance']['absent_slots']}
    """
    message.attach(MIMEText(body, "plain"))

    # Create an SMTP session
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, std["email"], message.as_string())

# Test data
std = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "attendance": {
        "percentage": 90,
        "total_slots": 20,
        "present_slots": 18,
        "absent_slots": 2
    }
}