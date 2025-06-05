from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
import time

#initialize driver
driver = init_driver()
driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-date-picker-demo")
time.sleep(2)

#find the input field for data picker
date_input = driver.find_element(By.ID, "birthday")

#enter a date directly into the input field
date_input.clear()
date_input.send_keys("2025-08-11")


time.sleep(2)
driver.quit()