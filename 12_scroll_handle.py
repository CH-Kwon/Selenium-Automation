from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
import time

driver = init_driver()
driver.get("https://the-internet.herokuapp.com/infinite_scroll")

#1. Scroll down for 5 times by using JavaScript

for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for new content to load
    
