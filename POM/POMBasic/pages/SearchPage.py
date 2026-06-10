from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self,driver):
        self.driver = driver
    def test_search(self, product):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(product)