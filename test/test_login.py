import sys
import os
import unittest
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Path setup
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import driver_setup
from pages.login_page import LoginPage
from locators.login_locator import LoginPageLocators as loc


class TestTC001_LoginValid(unittest.TestCase):

    def setUp(self):
        self.driver = driver_setup.init_driver()

    def test_tc001_login_with_valid_credentials(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")

        login_page = LoginPage(self.driver)

        # Tunggu sampai field username muncul
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.USERNAME_INPUT)
        )

        # Input data login
        login_page.enter_username("Admin")
        time.sleep(1)
        login_page.enter_password("admin123")
        time.sleep(1)
        login_page.click_login()
        time.sleep(3)

        # Tunggu sampai URL mengandung "dashboard"
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("dashboard")
        )
        self.assertIn("dashboard", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
