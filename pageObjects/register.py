import configparser

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


class Register:
    def __init__(self, driver, env):
        config = configparser.ConfigParser()
        config.read('../setting/config.ini')
        self.domain = config[env]['domain']
        self.url_signup = f"{self.domain}/signup.php"
        self.driver = driver

    def registration_form(self):
        return {
            'email': self.driver.find_element_by_id('exampleInputEmail1'),
            'password': self.driver.find_element_by_css_selector('input[type="password"][name="pwd"]'),
            'confirm_password': self.driver.find_element_by_css_selector('input[type="password"][name="repwd"]'),
            'name': self.driver.find_element_by_css_selector('input[name="name"]'),
            'year': Select(self.driver.find_element_by_css_selector('select[name="year"]')),
            'month': Select(self.driver.find_element_by_css_selector('select[name="month"]')),
            'agreement_checkbox': self.driver.find_element_by_css_selector('input[type="checkbox"][name="agree"]'),
        }

    def submit_registration(self):
        return self.driver.find_element_by_id("register-submit")

    def fill_form(self, data):
        self.driver.get(self.url_signup)
        self.registration_form()["email"].send_keys(data["email"])
        self.registration_form()["password"].send_keys(data["password"])
        self.registration_form()["confirm_password"].send_keys(data["password"])
        self.registration_form()["name"].send_keys(data["name"])
        self.registration_form()["year"].select_by_value(data["year"])
        self.registration_form()["month"].select_by_value(data["month"])
        self.registration_form()['agreement_checkbox'].click()
        self.submit_registration().click()

    def test_successful_registration(self, data):
        self.fill_form(data)
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            assert alert.text == "請至Email信箱 收驗證信! 謝謝！"
            alert.accept()
        except NoAlertPresentException:
            assert False, "Expected alert not present"

        assert self.driver.current_url == f"{self.domain}/login.php"
        return any(self.driver.find_elements_by_id('login-submit'))
