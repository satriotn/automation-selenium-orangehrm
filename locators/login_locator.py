from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON   = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
    ALERT_MESSAGE  = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")