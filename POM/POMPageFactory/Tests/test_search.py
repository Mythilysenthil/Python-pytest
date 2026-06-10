import pytest
from Utilities import excelReader
import Utilities.logCreater

from Pages.Homepage import HomePage
from Pages.Searchpage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    logger = Utilities.logCreater.log_creator()

  
    def test_validproduct(self):

        home_page = HomePage(self.driver)
        search_data = excelReader.get_data("TestData/SearchData.xlsx","Search")
        valid_product = search_data[0]
        home_page.enter_product_into_search_box(valid_product)
        home_page.click_search()
        self.logger.info("Valid product searched")
        search_page = SearchPage(self.driver)
        search_page.display_status_of_valid_product()
        self.logger.info("Valid product displayed")
    






    




