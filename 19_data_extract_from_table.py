from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#1. driver initialization
driver = init_driver()
driver.get("https://www.w3schools.com/")

#2. scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

#3. scroll to specific element
contact_link = driver.find_element(By.LINK_TEXT, "CONTACT US")
driver.execute_script("arguments[0].scrollIntoView();", contact_link)
time.sleep(2)

#4. check element visibility
print("Position:,", contact_link.location)
print("Size:", contact_link.size)

#5. Mouse hover test
ActionChains(driver).move_to_element(contact_link).perform()
time.sleep(2)

driver.quit()