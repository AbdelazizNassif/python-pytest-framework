from selenium.webdriver.common.by import By



class ShopPage():
    products_loc = (By.XPATH, "//div[@class='card h-100']")
    product_name_loc = (By.XPATH,  "div/h4/a")
    product_add_btn_loc = (By.XPATH, "div/button")
    check_out_btn_loc = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def __init__(self, driver):
        self.driver = driver

    def select_desired_product(self, desired_product):
        products = self.driver.find_elements(*ShopPage.products_loc)
        for product in products:
            product_name = product.find_element(*ShopPage.product_name_loc).text
            if product_name == desired_product:
                # Add item into cart
                product.find_element(*ShopPage.product_add_btn_loc).click()

    def click_checkout_btn(self):
        check_out_btn = self.driver.find_element(*ShopPage.check_out_btn_loc)
        check_out_btn.click()
