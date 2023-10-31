import pytest

from data.daten import signup_data
from pages.register_page import Register


class TestRegister:

    def test_successful_registration(self, setup, env):
        register = Register(setup, env)
        alert_present, alert_message, redirection, login_present = register.attempt_registration(signup_data)

        assert alert_present, "Expected alert not present"
        assert alert_message == "請至Email信箱 收驗證信! 謝謝！", f"Expected alert message, got {alert_message}"

        assert redirection == register.url_login, f"Expected {register.url_login}, got {redirection}"
        assert login_present, "Expected 'login-submit' element should be present"

    def test_register_with_invalid_email(self, setup, env):
        test_data = signup_data.copy()
        test_data["email"] = "invalid_email"

        register = Register(setup, env)
        alert_present, alert_message = register.invalid_data_registration(test_data)
        assert alert_present, "Expected alert not present"
        assert alert_message == "不符合email格式", f"Expected alert message, got {alert_message}"

    def test_register_confirm_password_not_match(self, setup, env):
        test_data = signup_data.copy()
        test_data["password_confirmed"] = "invalid_pwd"

        register = Register(setup, env)
        alert_present, alert_message = register.invalid_data_registration(test_data)
        assert alert_present, "Expected alert not present"
        assert alert_message == "密碼與確認密碼不符", f"Expected alert message, got {alert_message}"

    @pytest.mark.parametrize("field, value",
                             [("email", ""),
                              ("password_confirmed", ""),
                              ("name", ""), ])
    def test_register_field_empty(self, field, value, setup, env):
        test_data = signup_data.copy()
        test_data[field] = value

        register = Register(setup, env)
        alert_present, alert_message = register.invalid_data_registration(test_data)
        assert alert_present, "Expected alert not present"
        assert alert_message == "註冊資料有缺", f"Expected alert message, got {alert_message}"
