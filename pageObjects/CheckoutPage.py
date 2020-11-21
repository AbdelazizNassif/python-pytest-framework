from selenium.webdriver.common.by import By



class CheckoutPage():
    confirm_check_out_btn_loc = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def confirm_checkout(self):
        check_out_btn = self.driver.find_element(*CheckoutPage.confirm_check_out_btn_loc)
        check_out_btn.click()
