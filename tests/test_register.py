import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from TestData.HomePageData import HomePageData
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.DeliveryPage import DeliveryPage
from pageObjects.HomePage import HomePage
from pageObjects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


# child class (TestClassFw001) will automatically have knowledge of the fixture of the parents (BaseClass)
# Removing usefixture is OK now
class TestClassFw002(BaseClass):
    # self because it's inside class &  set_up because it uses the set_up method
    # after inherihance self now has driver in its structure
    def test_register(self, get_data):
        home_page_obj = HomePage(self.driver)
        log = self.get_logger()
        log.info("SSEECCOONNDD Test Case passed successfully")
        home_page_obj.enter_name(get_data["first_name"])
        home_page_obj.enter_email(get_data["email"])
        home_page_obj.enter_password(get_data["password"])
        home_page_obj.select_gender(get_data["gender"])
        home_page_obj.choose_employment_status(get_data["profession"])
        home_page_obj.click_submit()
        log.info("SSEECCOONNDD Test Case passed successfully")
        assert home_page_obj.check_success_message().is_displayed() == True
        assert 'Success' in home_page_obj.check_success_message().text
        self.driver.refresh()

    # data provider -> tests that will uset this function will exceute multiple times i.e 2 in this example
    # on iteration wil use only one tuple at a time
    @pytest.fixture(params=HomePageData.test_home_page_data)
    def get_data(self, request):
        return request.param

