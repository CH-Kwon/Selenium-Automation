from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = init_driver()
driver.get("https://the-internet.herokuapp.com/key_presses")

#1. input box search
input_box = driver.find_element(By.ID, "target")

#2. create single ActionChains object
input_box.send_keys("Keys.ENTER")
time.sleep(2)

#3. normal input
input_box.send_keys("Hello")
time.sleep(2)

#4. combination input
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(2)

driver.quit()