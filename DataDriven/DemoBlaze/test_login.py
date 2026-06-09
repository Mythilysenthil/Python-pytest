import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logCreator import log_generator
import read_config

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_login(self):
        logger = log_generator()
        logger.info("Login test started")
        self.driver.find_element(By.ID, "login2").click()
        logger.info("Clicked Login button")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "loginusername")))
        username = read_config.get_config("login info", "username")
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        logger.info(f"Entered username: {username}")
        password = read_config.get_config("login info", "password")
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        logger.info("Entered password")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))).click()
        logger.info("Clicked Log In")
        welcome_text = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "nameofuser"))).text
        logger.info(f"Welcome text: {welcome_text}")
        assert username in welcome_text
        logger.info("Login test passed")