from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

#1. setup download directory
download_dir = os.path.abspath("downloads")  # Ensure this directory exists
os.makedirs(download_dir, exist_ok=True)

#2 setup chromes download path
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_dir,  # Set the default download directory
    "download.prompt_for_download": False,  # Disable the download prompt
    "download.directory_upgrade": True,  # Allow directory upgrade
    "safebrowsing.enabled": True  # Enable safe browsing
}

options.add_experimental_option("prefs", prefs)

#3. driver initialization
driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/download")

#4.click the download link
file_link = driver.find_element(By.LINK_TEXT, "sample.txt")
file_link.click()

#5. wait for the download to complete
file_path = os.path.join(download_dir, "test-file.txt")

timeout = 10
while timeout > 0:
    if os.path.exists(file_path):
        print("Download completed successfully.", file_path)
        break
    time.sleep(1)
    timeout -= 1
else:
    print("download failed or timed out.")
    
time.sleep(5)
driver.quit()