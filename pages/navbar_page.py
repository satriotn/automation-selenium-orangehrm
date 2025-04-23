from selenium.webdriver.common.by import By
from locators.navbar_locator import NavbarLocators as nav_loc

class NavbarPage:
    def __init__(self, driver):
        self.driver = driver

    def click_pim(self):
        self.driver.find_element(By.XPATH, nav_loc.PIM).click()

    def click_leave(self):
        self.driver.find_element(By.XPATH, nav_loc.Leave).click()

    def click_time(self):
        self.driver.find_element(By.XPATH, nav_loc.Time).click()

    def click_recruitment(self):
        self.driver.find_element(By.XPATH, nav_loc.Recruitment).click()

    def click_my_info(self):
        self.driver.find_element(By.XPATH, nav_loc.MyInfo).click()

    def click_dashboard(self):
        self.driver.find_element(By.XPATH, nav_loc.Dashboard).click()

    def click_claim(self):
        self.driver.find_element(By.XPATH, nav_loc.Claim).click()
