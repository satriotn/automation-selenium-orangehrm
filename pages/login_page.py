from selenium.webdriver.remote.webdriver import WebDriver
from locators.login_locator import LoginPageLocators

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_username(self, username: str):
        self.driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password: str):
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_alert_message(self):
        return self.driver.find_element(*LoginPageLocators.ALERT_MESSAGE).text
