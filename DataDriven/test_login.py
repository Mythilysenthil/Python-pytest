from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from read_config import get_data

driver = None

def setup_function(function):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(get_data("config.ini", "basic info", "url"))

def teardown_function(function):
    global driver
    driver.quit()

def test_valid_product():
    driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys(get_data("config.ini", "key set", "valid_key"))
    driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys(Keys.ENTER)
    assert driver.find_element(By.XPATH, "//a[text() = \"HP LP3065\"]").is_displayed(), "The product is not displayed"

def test_invalid_product():
    driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys(get_data("config.ini", "key set", "invalid_key"))
    driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys(Keys.ENTER)
    assert driver.find_element(By.XPATH, "//p[text() = \"There is no product that matches the search criteria.\"]").is_displayed(), "No product message is not displayed"

def test_no_product():
    driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys("")
    driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys(Keys.ENTER)
    assert driver.find_element(By.XPATH, "//p[text() = \"There is no product that matches the search criteria.\"]").is_displayed(), "No product message is not displayed"