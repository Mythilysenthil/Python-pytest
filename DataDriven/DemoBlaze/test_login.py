import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import read_config

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_login(self):
        self.driver.find_element(By.ID, "login2").click()
        username = read_config.get_config("login info", "username")
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        password = read_config.get_config("login info", "password")
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        welcome_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "nameofuser"))).text
        assert username in welcome_text