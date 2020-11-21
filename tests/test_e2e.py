import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.DeliveryPage import DeliveryPage
from pageObjects.HomePage import HomePage
from pageObjects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


# child class (TestClassFw001) will automatically have knowledge of the fixture of the parents (BaseClass)
# Removing usefixture is OK now

class TestClassFw001(BaseClass):
    # self because it's inside class &  set_up because it uses the set_up method
    # after inherihance self now has driver in its structure
    def test_e2e(self):
        home_page_obj = HomePage(self.driver)
        shop_page_obj = ShopPage(self.driver)
        check_out_page_obj = CheckoutPage(self.driver)
        delivery_page_obj = DeliveryPage(self.driver)
        log = self.get_logger()
        home_page_obj.click_shop()
        log.info("Clicking Shop Link Successfully")
        shop_page_obj.select_desired_product("BlackBerry")
        log.info("Selecting BlakBerry")
        shop_page_obj.click_checkout_btn()
        check_out_page_obj.confirm_checkout()
        delivery_page_obj.select_delivery_country()
        delivery_page_obj.agree_terms_with_app()
        delivery_page_obj.submit_purchase()
        assert "Success! Thank you!" in delivery_page_obj.get_success_message()
        log.info("first Test Case passed successfully")
