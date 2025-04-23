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
from pages.pim_page import PimPage
from locators.navbar_locator import NavbarLocators as navloc
from locators.login_locator import LoginPageLocators as logloc
from locators.pim_locator import PimLocators as pimloc


class TestPIM(unittest.TestCase):

    def setUp(self):
        self.driver = driver_setup.init_driver()
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.login_page = LoginPage(self.driver)
        self.pim_page = PimPage(self.driver)

        # Tunggu sampai field username muncul
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(logloc.USERNAME_INPUT)
        )

        # Input data login
        time.sleep(3)
        self.login_page.enter_username("Admin")
        time.sleep(1)
        self.login_page.enter_password("admin123")
        time.sleep(1)
        self.login_page.click_login()
        time.sleep(3)

        # Tunggu sampai URL mengandung "dashboard"
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("dashboard")
        )
        self.assertIn("dashboard", self.driver.current_url)

        # Tunggu navbar muncul
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, navloc.PIM))
        )

        print("✅ Setup berhasil: Login dan navigasi awal sukses")

    def test_add_employee(self):
        
        time.sleep(3)
        # Klik tombol PIM
        self.driver.find_element(By.XPATH, navloc.PIM).click()

        time.sleep(3)
        # Verifikasi kita berada di halaman PIM
        self.pim_page.verify_pim_page()

        # Klik tombol Add
        self.pim_page.click_add_employee()

        # Isi nama lengkap dan ID  
        self.pim_page.enter_basic_employee_info(
            firstname="Budi",
            middlename="T",
            lastname="Santoso",
            employee_id="123456"
        )

        # Aktifkan switch login dan isi detail login
        self.pim_page.enable_login_details_section()
        time.sleep(3)  # Tunggu animasi toggle
        self.pim_page.fill_login_details(
            username="budisantoso8",
            password="budi123",
            confirm_password="budi123",
            status="enable"
        )

        time.sleep(3)
        alert_message = self.pim_page.get_alert_message()
        self.assertIn("Username already exists", alert_message)
        print(f"✅ Alert muncul: {alert_message}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
