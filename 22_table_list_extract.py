from utils.driver_setup import init_driver
from selenium.webdriver.common.by import By
import time

# 1. Initialize the driver and open the website
driver = init_driver()
driver.get("https://quotes.toscrape.com/scroll")

time.sleep(2)  # Allow the page to load

prev_count = 0

# 2. Scroll repeatedly until no new quotes are loaded
while True:
    # Find all currently loaded quote elements
    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    print(f"🧾 Current quote count: {len(quotes)}")

    # If the number of quotes hasn't increased, break the loop
    if len(quotes) == prev_count:
        print("All quotes loaded")
        break

    # Update the previous count
    prev_count = len(quotes)

    # Scroll to the bottom of the page to trigger loading more content
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for new quotes to load

# 3. Print out all the quotes
for quote in quotes:
    print("quote: ", quote.text.strip())

driver.quit()