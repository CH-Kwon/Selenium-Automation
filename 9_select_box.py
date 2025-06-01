#utils/driver_init.py
from utils.driver_setup import init_driver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

# driver initialization from utils
driver = init_driver()

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")

driver.switch_to.frame("iframeResult")

select_element = driver.find_element(By.ID,"cars")
dropdown = Select(select_element)

dropdown.select_by_visible_text("Saab")
time.sleep(2)

dropdown.select_by_value("audi")
time.sleep(2)

dropdown.select_by_index(0)
time.sleep(2)

driver.quit()