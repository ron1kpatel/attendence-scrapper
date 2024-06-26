from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from constant import *
import mail
import Helper

# Set Chrome options for a visible window
options = Options()
options.add_argument("--headless=false")  # Disables headless mode

# Create a new Service object (adjust path if needed)
service = Service("chromedriver")

# Create the WebDriver instance with options
driver = webdriver.Chrome(service=service, options=options)

# Log in to the website
logged_in_driver = Helper.login(driver)

# Get student details and attendance
wait = WebDriverWait(logged_in_driver, 10)
std = Helper.getStudentDetailsAndAttendance(logged_in_driver, wait)
# Quit the WebDriver
driver.quit()

# Send email with student details and attendance
mail.sendMail(std)