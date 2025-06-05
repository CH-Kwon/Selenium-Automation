from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#1. Driver initialization and URL loading
driver = init_driver()
driver.get("https://books-pwakit.appspot.com/")

time.sleep(2)

#2. shadow-root element access (need JS)
host_element = driver.find_element(By.CSS_SELECTOR, "book-app")
shadow_root = driver.execute_script("return arguments[0].shadowRoot", host_element)

#3. find input element inside shadow-root
search_input = shadow_root.find_element(By.CSS_SELECTOR, "app-header > app-toolbar > book-input-decorator > input")

#4. enter text into the input field
search_input.send_keys("Python")
search_input.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
