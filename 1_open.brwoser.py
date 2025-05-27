from utils.driver_setup import init_driver
import time

def open_google():
    driver = init_driver()
    driver.get("https://www.google.com")
    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    open_google()