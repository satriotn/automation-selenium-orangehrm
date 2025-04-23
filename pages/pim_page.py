# pim_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.pim_locator import PimLocators as pim_loc

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_pim_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, pim_loc.HEADER))
        )
        header_text = self.driver.find_element(By.XPATH, pim_loc.HEADER).text.strip()
        assert "PIM" in header_text, "❌ Bukan di halaman PIM"


    def click_add_employee(self):
        self.driver.find_element(By.XPATH, pim_loc.ADD_BUTTON).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, pim_loc.HEADER_ADD_EMPLOYEE)))

    def enter_basic_employee_info(self, firstname, middlename, lastname, employee_id):
        self.driver.find_element(By.XPATH, pim_loc.FIRSTNAME).send_keys(firstname)
        self.driver.find_element(By.XPATH, pim_loc.MIDDLENAME).send_keys(middlename)
        self.driver.find_element(By.XPATH, pim_loc.LASTNAME).send_keys(lastname)
        self.driver.find_element(By.XPATH, pim_loc.EMPLOYEE_ID).clear()
        self.driver.find_element(By.XPATH, pim_loc.EMPLOYEE_ID).send_keys(employee_id)

    def enable_login_details_section(self):
        self.driver.find_element(By.XPATH, pim_loc.SWITCH_EMPLOYEE_DETAIL_LOGIN).click()
        # Tunggu elemen login muncul
        self.wait.until(EC.visibility_of_element_located((By.XPATH, pim_loc.USERNAME)))

    def fill_login_details(self, username, password, confirm_password, status='enabled'):
        self.driver.find_element(By.XPATH, pim_loc.USERNAME).send_keys(username)
        self.driver.find_element(By.XPATH, pim_loc.PASSWORD).send_keys(password)
        self.driver.find_element(By.XPATH, pim_loc.CONFIRM_PASSWORD).send_keys(confirm_password)

        if status.lower() == 'enabled':
            self.driver.find_element(By.XPATH, pim_loc.RADIO_BUTTON_STATUS_ENABLE).click()
        elif status.lower() == 'disabled':
            self.driver.find_element(By.XPATH, pim_loc.RADIO_BUTTON_STATUS_DISABLE).click()

    def verify_user(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, pim_loc.ASSERTASSERT_FIELD))
            )
            print("✅ Header ditemukan")
        except:
            print("❌ Header tidak ditemukan")

    def verify_user_redirected(self):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("viewPersonalDetails")
        )
        current_url = self.driver.current_url
        assert "viewPersonalDetails" in current_url, "❌ Tidak diarahkan ke halaman detail karyawan"

    def get_alert_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".oxd-input-field-error-message").text

    
    def click_save(self):
        self.driver.find_element(By.XPATH, pim_loc.SAVE_BUTTON).click()
