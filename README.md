# Selenium Automation Practice (Python)

This is personal portfolio project where I am learning Selnium step by step using Python.
Each script is kind a small but hands-on experience focused on core automation skills that QA Engineer actually use in real world.

# Getting Started
```bash
git clone https://github.com/your-username/selenium-automation.git
cd selenium-automation
python -m venv venv
venv\Scripts\activate  # For Windows
pip install -r requirements.txt

## Project Structure

* 01_open_browser.py: 
    - Very first steip for opening browser and visiting URL
    - This is super simple, just using driver.get() to check that everything runs ok.
    - Website: Google

* 02_find_elements.py: 
    - Basic element interation: find the search input on DuckDuckGo and sumit a query
    - Practicing with 'find_element()', 'send_keys()', and '.submit()'
    - Website: DuckDuckGo

* 03_user_input.py: 
    - Introduced WebDriverWait and ExpectedCondition to handle slower-loading elements.
    - Practiced waiting for search result element to show up before extracting its content.
    - Website: DuckDuckGo

* 04_waits.py: 
    - Introduced 'WebDriverWait' and 'ExpectedConditions' to handle slower-loading elements.
    - Practiced waiting for a search result element to show up before extracting its content.
    - Website: DuckDuckGo

* 05_classname_text.py: 
    - Collected multiple elements with the same class and printed their text.
    - good for simulating things like scarping headlines,list, etc
    - Website: DuckDuckGo

* 06_action_chain.py:
    - This one is pretty fun - I got to implement mouse action like right-click and double-click
    - Leanred how to deal with alert pop-up
    @ what happends in this script
        - Right click on the "Right click me" button
        - Select "Copy" from the context menu -> handle the alert that pops up
        - Double-click on the "Double-Click Me To see Alert" button -> handle the second alert
    @ Covered skills:
        - "ActionChains.context_click()" and ".double_click()"
        - "WebDriverWait" with "alert_is_present()
        - driver.switch_to.alaert.accept()
    - Website: https://demo.guru99.com/test/simple_context_menu.html
