from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
import time

def get_titles():
    driver = init_driver()
    driver.get("https://duckduckgo.com")
    driver.find_element(By.NAME, "q").send_keys("Selenium WebDriver")
    driver.find_element(By.NAME, "q").submit()
    time.sleep(3)
    
    elements = driver.find_elements(By.CSS_SELECTOR, ".result__a")
    for el in elements[:5]:
        print(el.text)
    driver.quit()

if __name__ == "__main__":
    get_titles()