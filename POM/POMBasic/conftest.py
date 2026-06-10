import selenium
from selenium import webdriver
from configuration import read_config
import pytest
import Utilities.logCreator

@pytest.fixture()
def setup_and_teardown(request):
    logger = Utilities.logCreator.log_generator()
    browser = read_config.get_data("basic info","browser")
    if browser=="chrome":
        driver = webdriver.Chrome()
    elif browser=="Edge":
        driver = webdriver.Edge()
    elif browser=="Firefox":
        driver = webdriver.Firefox()
    logger.info("Browser launched")
    driver.maximize_window()

    url = read_config.get_data("basic info","url")
    driver.get(url)
    logger.info("Application launched")
    request.cls.driver = driver
    
    yield
    
    driver.quit()