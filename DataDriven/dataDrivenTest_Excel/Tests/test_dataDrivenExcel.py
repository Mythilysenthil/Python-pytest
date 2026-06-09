import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities import excelReader
import utilities.logCreator as logCreator

EXCEL_PATH = r"C:\Users\Navee\OneDrive\Documents\Expleo training\python\Pytest\DataDriven\dataDrivenTest_Excel\Excelfiles\loginData.xlsx"
log = logCreator.log_generator()

@pytest.mark.parametrize("username,password", excelReader.get_data(EXCEL_PATH, "Sheet1"))
class TestLogin1:

    def test_login(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        log.info(f"Testing login for user: {username}")
        self.driver.find_element(By.ID, "login2").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        time.sleep(5)

        if EC.alert_is_present()(self.driver):
            alert = self.driver.switch_to.alert
            assert alert.text == "Wrong password.", f"Unexpected alert: {alert.text}"
            alert.accept()
            log.warning(f"Invalid login for user: {username}")
        else:
            welcome = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "nameofuser"))).text
            assert username in welcome, f"Valid login failed for: {username}"
            log.info(f"Login successful: {welcome}")
        self.driver.quit()