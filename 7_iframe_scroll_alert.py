from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def iframe_scroll_alert_example():
    driver = init_driver()
    driver.get("https://demo.automationtesting.in/Alerts.html")
    
    wait = WebDriverWait(driver, 10)
    
    #1. Alert with OK button
    alert_ok_tab = driver.find_element(By.XPATH, "//a[@href='#OKTab']")
    alert_ok_tab.click()
    time.sleep(2)
    
    #2. Button to trigger alert
    alert_btn = driver.find_element(By.XPATH, "//button[contains(text(),'alert box:')]")
    alert_btn.click()
    
    #3. alaert handling
    alert = wait.until(EC.alert_is_present())
    print("Alert text:", alert.text)
    alert.accept()
    time.sleep(2)    
    #4. Alert with textbox tap click
    textbox_tab = driver.find_element(By.XPATH, "//a[contains(text(),'Alert with Textbox')]")
    textbox_tab.click()
    time.sleep(2)
    
    #5 Butgton click -> prompt alert
    prompt_btn = driver.find_element(By.XPATH,"//button[contains(text(), 'prompt box')]")
    prompt_btn.click()
    time.sleep(2)
    
    #6. alaert text input + confirm
    alert = wait.until(EC.alert_is_present())
    print("Prompt Text:", alert.text)
    time.sleep(2)
    alert.send_keys("Hello")
    alert.accept()
    time.sleep(1)
    
    driver.quit()
    
if __name__ == "__main__":
    iframe_scroll_alert_example()
    