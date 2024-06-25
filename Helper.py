from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constant import *
def login(driver):
    # Navigate to the URL
    driver.get("https://ums.paruluniversity.ac.in")

    # Wait until the radio button is clickable and then click it
    wait = WebDriverWait(driver, 10)
    radio_button = wait.until(EC.element_to_be_clickable((By.ID, "rblRole_1")))
    radio_button.click()

    # Fill in the email input
    email_input = driver.find_element(By.ID, "txtUsername")
    email_input.clear()
    email_input.send_keys(email)

    # Fill in the password input
    password_input = driver.find_element(By.ID, "txtPassword")
    password_input.clear()
    password_input.send_keys(password)

    # Click the submit button
    submit_button = driver.find_element(By.ID, "btnLogin")
    submit_button.click()

    # Wait for the error message to appear (if any) and print it
    try:
        error_message = wait.until(EC.visibility_of_element_located((By.ID, "ucMessage_lblError")))
        print("Error message:", error_message.text)
        return {status: False, message:error_message.text}
    except:
        return driver
def getStudentDetailsAndAttendence(driver, wait):
    driver.get("https://ums.paruluniversity.ac.in/StudentPanel/StudentDashboard.aspx")

    student_name_span = wait.until(EC.visibility_of_element_located((By.ID, "ctl00_cphPageContent_ucStudentInfoCompact_lblStudentLCName")))

    student_enroll_span = wait.until(EC.visibility_of_element_located((By.ID, "ctl00_cphPageContent_ucStudentInfoCompact_lblEnrollmentNo")))
    student_name = student_name_span.text
    student_enroll = student_enroll_span.text

    driver.get(attendence)

    total_slot = driver.find_element(By.ID, "ctl00_cphPageContent_lblTotalLectureLabCount").text
    present_slot = driver.find_element(By.ID, "ctl00_cphPageContent_lblPresentLectureLabCount").text
    absent_slot = driver.find_element(By.ID, "ctl00_cphPageContent_lblAbsentLectureLabCount").text
    percentage = driver.find_element(By.ID, "ctl00_cphPageContent_lblPresentPCTCount").text

    print(f"Total Lecture/Lab: {total_slot}")
    print(f"Present Lecture/Lab: {present_slot}")
    print(f"Absent Lecture/Lab: {absent_slot}")
    print(f"Percentage: {percentage}")

    std = {
        "name": student_name,
        "enroll": student_enroll,
        "email": student_enroll+"@paruluniversity.ac.in",
        "attendance": {
            "percentage": percentage,
            "total_slots": total_slot,
            "present_slots":present_slot,
            "absent_slots": absent_slot
        }

    }
    return std

