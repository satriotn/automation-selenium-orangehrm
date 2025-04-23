# openMRS/utils/driver_setup.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

def init_driver():
    driver_path = os.path.join(os.getcwd(), "drivers", "chromedriver.exe")
    service = Service(driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(service=service, options=options)
    return driver