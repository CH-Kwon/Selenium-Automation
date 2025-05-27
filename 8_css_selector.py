from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
import time

def css_selector_example():
    driver = init_driver()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    
    time.sleep(2)
    
    #1. input field using id selector
    input_field = driver.find_element(By.CSS_SELECTOR,"#my-text-id")
    input_field.send_keys("Hello CSS")
    time.sleep(3)
    
    #2., submit button using class selector
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn-outline-primary")
    submit_button.click()
    time.sleep(3)
    
    driver.quit()
    
if __name__ == "__main__":
    css_selector_example()
        