from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
import time

driver = init_driver()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

try:
    #1. show up alaert
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    time.sleep(3)
    
    #2. alaert handling
    alert = Alert(driver)
    print("Alert text:", alert.text)
    alert.accept()  # Accept the alert
    
except NoAlertPresentException:
    print("No alert present.")
except Exception as e:
    print("Unexpected error:", str(e))
    
finally:
    time.sleep(3)
    driver.quit()