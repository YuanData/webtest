import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def setup():
    driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture
def env():
    """
    Provides the environment for the test.
    Available environments are:
    - PROD
    - UAT
    - QA

    :return: str - The environment for the test. Default is "UAT".
    """
    return "UAT"
