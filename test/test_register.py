import pageObjects.register as register
from data.daten import correct_data


def test_register(setup):
    assert register.Register(setup, env="PROD").test_successful_registration(correct_data)
