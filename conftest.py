import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(executable_path='../drivers/chromedriver', options=chrome_options)

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
