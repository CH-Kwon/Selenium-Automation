from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
import time

#1. driver initialization
driver = init_driver()
driver.get("https://w3schools.com/html/html_forms.asp")

time.sleep(2)

#2. insert value to the JS  
name_input = driver.find_element(By.ID, "fname")
driver.execute_script("arguments[0].value = 'John';",name_input)

#3. border style change by JS   
driver.execute_script("arguments[0].style.border = '3px solid red';", name_input)

#4. check current scroll
scroll_y = driver.execute_script("return window.scrollY;")   
print("Current scroll position:", scroll_y)

#5. get page title
title = driver.execute_script("return document.title;")
print("page title:", title)

#6. scroll to the top of the page
driver.execute_script("window.scrollTo(0, 0);")

time.sleep(2)
driver.quit()