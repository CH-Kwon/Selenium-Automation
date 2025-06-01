from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = init_driver()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")

#1. find drag and drop elements
source = driver.find_element(By.ID, "column-a")
target = driver.find_element(By.ID, "column-b")

#2. Create an ActionChains object
actions = ActionChains(driver)

#3. Perform drag and drop
actions.drag_and_drop(source,target).perform()

time.sleep(2)
driver.quit()


