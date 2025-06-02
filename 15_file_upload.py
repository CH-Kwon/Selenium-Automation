from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
import time
import os

driver = init_driver()
driver.get("https://the-internet.herokuapp.com/upload")

#1. setup the path to the file
file_path = os.path.abspath("sample.txt") # sample.txt should be in the same directory as this script

#2. <input type="file"> element file path 
file_input = driver.find_element(By.ID, "file-upload")
file_input.send_keys(file_path)

#3. click the upload button
driver.find_element(By.ID, "file-submit").click()

time.sleep(2)
driver.quit()