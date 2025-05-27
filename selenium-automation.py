from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    # Open a website and perform a search
    driver.get("https://www.example.com")
    print("Opened google website")
    
    # implicitly wait for elements to load
    driver.WebDriverWait(driver, 10)
    search_box = driver.find_element(By.NAME, "q")
    print("Search box found")
    
    search_term = "Today's weather"
    search_box.send_keys(search_term)
    print(f"'{search_term}' entered in search box")
    
    search_box.submit()
    print("Search submitted")
    
    time.sleep(3)
    print(f"Current page title: {driver.title}")
    
    assert search_term in driver.title, f"'{search_term} not found in page title" 
    
    print("test passed")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'driver' in locals() and driver is not None:
        driver.quit()
        print("Browser closed")