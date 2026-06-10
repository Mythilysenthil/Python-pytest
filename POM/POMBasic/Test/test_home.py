import pytest
from pages.loginPage import LoginPage
from pages.SearchPage import SearchPage
from Utilities.ExcelReader import get_data

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    @pytest.mark.parametrize("username,password",get_data("Excel/Book1.xlsx", "Sheet1"))
    def test_valid_login(self, username, password):
        login = LoginPage(self.driver)
        login.test_login(username, password)

    @pytest.mark.parametrize("product",get_data("Excel/Book1.xlsx", "search"))
    def test_valid_search(self, product):
        search = SearchPage(self.driver)
        search.test_search(product)