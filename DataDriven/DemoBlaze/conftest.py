import pytest
from selenium import webdriver
import read_config

@pytest.fixture()
def setup_and_teardown(request):
    browser = read_config.get_config("basic info", "browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(read_config.get_config("basic info", "url"))
    request.cls.driver = driver

    yield
    driver.quit()