from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
import time

#1. execute driver
driver = init_driver()
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(2)

#2. find the table element
table = driver.find_element(By.ID, "customers")
rows = table.find_elements(By.TAG_NAME, "tr")

#3. extract the cell data from each row
for row in rows[1:]:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) > 0:
        company_name = cells[0].text
        print("Company Name:", company_name)

driver.quit()