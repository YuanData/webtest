import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def setup():
    driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
    driver.maximize_window()
    yield driver
    driver.close()
