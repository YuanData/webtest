import configparser

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from config_manager import ConfigManager
from locators.register_loc import *


def load_domain(env):
    config = configparser.ConfigParser()
    config.read('../setting/config.ini')
    return config[env]['domain']


class Register:
    def __init__(self, driver, env):
        config_manager = ConfigManager()
        self.domain = config_manager.get_domain(env)
        self.url_signup = f"{self.domain}/signup.php"
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url_signup)

        # Initialize instance attributes
        self.email = None
        self.password = None
        self.confirm_password = None
        self.name = None
        self.year = None
        self.month = None
        self.agreement_checkbox = None
        self.register_submit = None

        self.load_elements()

    def load_elements(self):
        self.email = self.driver.find_element_by_id(EMAIL)
        self.password = self.driver.find_element_by_css_selector(PASSWORD)
        self.confirm_password = self.driver.find_element_by_css_selector(CONFIRM_PASSWORD)
        self.name = self.driver.find_element_by_css_selector(NAME)
        self.year = Select(self.driver.find_element_by_css_selector(YEAR))
        self.month = Select(self.driver.find_element_by_css_selector(MONTH))
        self.agreement_checkbox = self.driver.find_element_by_css_selector(AGREEMENT_CHECKBOX)
        self.register_submit = self.driver.find_element_by_id(REGISTER_SUBMIT)

    def fill_form(self, data):
        self.email.send_keys(data["email"])
        self.password.send_keys(data["password"])
        self.confirm_password.send_keys(data["password"])
        self.name.send_keys(data["name"])
        self.year.select_by_value(data["year"])
        self.month.select_by_value(data["month"])
        self.agreement_checkbox.click()
        self.register_submit.click()

    def test_successful_registration(self, data):
        self.fill_form(data)
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            assert alert.text == "請至Email信箱 收驗證信! 謝謝！"
            alert.accept()
        except NoAlertPresentException:
            assert False, "Expected alert not present"

        assert self.driver.current_url == f"{self.domain}/login.php"
        return any(self.driver.find_elements_by_id('login-submit'))
