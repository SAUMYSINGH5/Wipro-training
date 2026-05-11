from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import LogGen

logger = LogGen.loggen()


class SignupPage:

    signup_menu = (By.ID, "signin2")
    username_input = (By.ID, "sign-username")
    password_input = (By.ID, "sign-password")
    signup_button = (By.XPATH, "//button[text()='Sign up']")

    def __init__(self, driver):
        self.driver = driver

    def click_signup_menu(self):
        logger.info("Click signup menu")
        self.driver.find_element(*self.signup_menu).click()

    def enter_username(self, username):
        logger.info(f"Enter username: {username}")
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        logger.info("Enter password")
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_signup_button(self):
        logger.info("Click signup button")
        self.driver.find_element(*self.signup_button).click()

    def verify_signup_success(self):

        try:
            wait = WebDriverWait(self.driver, 10)
            alert = wait.until(EC.alert_is_present())

            text = alert.text
            alert.accept()

            return text

        except TimeoutException:
            return "No alert appeared"