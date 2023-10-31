from data.daten import correct_data
from pages.register_page import Register


def test_register(setup):
    register = Register(setup, env="PROD")
    alert_present, alert_message, redirection, login_present = register.attempt_registration(correct_data)

    assert alert_present, "Expected alert not present"
    assert alert_message == "請至Email信箱 收驗證信! 謝謝！", f"Expected alert message, got {alert_message}"
    assert redirection == register.url_login, f"Expected {register.url_login}, got {redirection}"
    assert login_present, "Expected 'login-submit' element to be present"
