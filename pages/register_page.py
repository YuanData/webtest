from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from config_manager import ConfigManager
from locators.register_loc import *


class Register:
    def __init__(self, driver, env):
        config_manager = ConfigManager()
        self.domain = config_manager.get_domain(env)
        self.url_signup = f"{self.domain}/signup.php"
        self.url_login = f"{self.domain}/login.php"

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url_signup)

    def fill_form(self, data):
        self.driver.find_element_by_id(EMAIL).send_keys(data["email"])
        self.driver.find_element_by_css_selector(PASSWORD).send_keys(data["password"])
        self.driver.find_element_by_css_selector(CONFIRM_PASSWORD).send_keys(data["password_confirmed"])
        self.driver.find_element_by_css_selector(NAME).send_keys(data["name"])
        Select(self.driver.find_element_by_css_selector(YEAR)).select_by_value(data["year"])
        Select(self.driver.find_element_by_css_selector(MONTH)).select_by_value(data["month"])
        self.driver.find_element_by_css_selector(AGREEMENT_CHECKBOX).click()
        self.driver.find_element_by_id(REGISTER_SUBMIT).click()

    def attempt_registration(self, data):
        self.fill_form(data)
        alert_message = None
        alert_present = False
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_message = alert.text
            alert.accept()
            alert_present = True
        except NoAlertPresentException:
            pass

        redirection = self.driver.current_url
        login_present = any(self.driver.find_elements_by_id('login-submit'))

        return alert_present, alert_message, redirection, login_present

    def invalid_data_registration(self, data):
        self.fill_form(data)
        alert_message = None
        alert_present = False
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_message = alert.text
            alert.accept()
            alert_present = True
        except NoAlertPresentException:
            pass

        return alert_present, alert_message
