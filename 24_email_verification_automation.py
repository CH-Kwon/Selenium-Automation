from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
import time

driver = init_driver()
driver.get("https://mail.tm/en/")

# Wait for email to load
time.sleep(6)

# Find the input box that contains the email address
email_input = driver.find_element(By.CSS_SELECTOR, "input[readonly]")
temp_email = email_input.get_attribute("value")

print("Temp Email:", temp_email)

driver.quit()