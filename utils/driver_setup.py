from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def init_driver(headless=False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--start-maximized")
    service = Service()
    return webdriver.Chrome(service=service, options=options)