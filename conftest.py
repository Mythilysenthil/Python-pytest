import pytest
from selenium import webdriver

@pytest.fixture
def setup_and_teardown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
    yield driver
    driver.quit()