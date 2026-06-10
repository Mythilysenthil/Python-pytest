from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self,driver):
        self.driver = driver
    def test_login(self, username, password):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Login']").click()
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()