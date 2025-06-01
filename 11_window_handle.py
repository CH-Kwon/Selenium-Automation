from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
import time

driver = init_driver()
driver.get("https://the-internet.herokuapp.com/windows")

#1. save handle of current window
main_window = driver.current_window_handle

#2. open the new window by clicking the "click here"
driver.find_element(By.XPATH, "//a[text()='Click Here']").click()
time.sleep(3)

#3. get all window handles
all_windows = driver.window_handles

#4. switching focus to the new window
for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        break

#5. perform actions in the new window
print("New Window Title: ", driver.title)

#6. back to the main window
driver.switch_to.window(main_window)
print("Back to the main window title: ", driver.title)

time.sleep(2)
driver.quit()
