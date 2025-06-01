from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = init_driver()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# normal alaert handle
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = Alert(driver)
time.sleep(1)
alert.accept()  # Accept the alert

#2. Confirm alert handle
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
alert = Alert(driver)
time.sleep(1)
alert.dismiss()

#3. prompt alert handle
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
alaert = Alert(driver)
time.sleep(1)
alaert.send_keys("Put text")
alaert.accept()

time.sleep(2)
driver.quit()
