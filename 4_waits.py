from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_example():
    driver = init_driver()
    driver.get("https://duckduckgo.com")
    search = driver.find_element(By.NAME, "q")
    search.send_keys("WebDriverWait Selenium")
    search.submit()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".result__a"))
    )

    links = driver.find_elements(By.CSS_SELECTOR, ".result__a")
    for link in links[:5]:
        print(link.text)
    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    wait_example()