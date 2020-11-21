from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DeliveryPage():
    country_box_loc = (By.ID, "country")
    india_country_loc = (By.LINK_TEXT, "India")
    agree_terms_loc = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_btn_loc = (By.CSS_SELECTOR, "[type='submit']")
    success_msg_loc = (By.CLASS_NAME, "alert-success")
    # successText = self.driver.find_element_by_class_name("alert-success").text
    """self.driver.find_element_by_id("country").send_keys("ind")
        wait = WebDriverWait(self.driver, 7)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()"""

    def __init__(self, driver):
        self.driver = driver
        self.exp_wait = WebDriverWait(self.driver, 7)

    def select_delivery_country(self):
        country_box = self.driver.find_element(*DeliveryPage.country_box_loc)
        country_box.send_keys("ind")
        self.exp_wait.until(EC.presence_of_element_located(DeliveryPage.india_country_loc))
        india_country = self.driver.find_element(*DeliveryPage.india_country_loc)
        india_country.click()

    def agree_terms_with_app(self):
        agree_terms = self.driver.find_element(*DeliveryPage.agree_terms_loc)
        agree_terms.click()

    def submit_purchase(self):
        purchase_btn = self.driver.find_element(*DeliveryPage.purchase_btn_loc)
        purchase_btn.click()

    def get_success_message(self):
        success_msg = self.driver.find_element(*DeliveryPage.success_msg_loc)
        return success_msg.text



