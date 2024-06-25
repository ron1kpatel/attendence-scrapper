from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
driver = Helper.login(driver)
wait = WebDriverWait(driver, 10);




std = Helper.getStudentDetailsAndAttendence(driver, wait)

mail.sendMail(std)
print(std)
driver.quit();
