from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
import time

def input_example():
    driver = init_driver()
    driver.get("https://duckduckgo.com")
    first_input = driver.find_element(By.NAME, "q")
    first_input.clear()
    first_input.send_keys("Selenium Python")
    first_input.submit()
    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    input_example()