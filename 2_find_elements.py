from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
import time

def search_duckduckgo():
    driver = init_driver()
    driver.get("https://duckduckgo.com")
    search_input = driver.find_element(By.NAME, "q")
    search_input.send_keys("Selenium Python")
    search_input.submit()
    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    search_duckduckgo()