from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class HomePage():
    shop_loc = (By.CSS_SELECTOR, "a[href*='shop']")
    name_loc = (By.CSS_SELECTOR, "input[name='name']")
    email_loc = (By.CSS_SELECTOR, "input[name='email']")
    password_loc = (By.ID, "exampleInputPassword1")
    gender_dd_list_loc = (By.ID, "exampleFormControlSelect1")
    student_loc = (By.ID, "inlineRadio1")
    employee_loc = (By.ID, "inlineRadio2")
    submit_btn_loc = (By.CSS_SELECTOR, "input[type = 'submit']")
    success_msg_loc = (By.CSS_SELECTOR, "div.alert-success")

    def __init__(self, driver):
        self.driver = driver

    def click_shop(self):
        shop_link = self.driver.find_element(*HomePage.shop_loc)
        shop_link.click()

    def enter_name(self, user_name):
        name_box = self.driver.find_elements(*HomePage.name_loc)[0]
        name_box.send_keys(user_name)

    def enter_email(self, user_email):
        email_box = self.driver.find_element(*HomePage.email_loc)
        email_box.send_keys(user_email)

    def enter_password(self, user_password):
        password_box = self.driver.find_element(*HomePage.password_loc)
        password_box.send_keys(user_password)

    def select_gender(self, user_gender):
        gender_list = Select(self.driver.find_element(*HomePage.gender_dd_list_loc))
        if user_gender == 'male':
            gender_list.select_by_visible_text('Male')
        elif user_gender == 'female':
            gender_list.select_by_visible_text('Female')

    def choose_employment_status(self, user_emp_status):
        if user_emp_status == 'student':
            student_rad_btn = self.driver.find_element(*HomePage.student_loc)
            student_rad_btn.click()
        elif user_emp_status == 'employee':
            employee_rad_btn = self.driver.find_element(*HomePage.employee_loc)
            employee_rad_btn.click()

    def click_submit(self):
        submit_btn = self.driver.find_element(*HomePage.submit_btn_loc)
        submit_btn.click()

    def check_success_message(self):
        success_msg = self.driver.find_element(*HomePage.success_msg_loc)
        self.driver.execute_script('arguments[0].scrollIntoView()' , success_msg)
        return success_msg

