from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def action_chains_example():
    driver = init_driver()
    driver.get("https://demo.guru99.com/test/simple_context_menu.html")

    actions = ActionChains(driver)
    
    # Right-click on the button
    right_click_btn = driver.find_element(By.XPATH, "//span[text()='right click me']")
    actions.context_click(right_click_btn).perform()
    time.sleep(2)
    
    #copy option in context menu
    copy_option = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//span[text()='Copy']")))
    copy_option.click()
    time.sleep(2)
    
    # alert handling
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()
    time.sleep(1)
    
    # doble-click on the button
    double_click_btn = driver.find_element(By.XPATH, "//button[text()='Double-Click Me To See Alert']")
    actions.double_click(double_click_btn).perform()
    time.sleep(2)
    
    driver.quit()
    
if __name__ == "__main__":
     action_chains_example()
