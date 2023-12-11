from selenium.webdriver.common.by import By
from features.pages.account_page import AccountPage
from features.pages.base_page import BasePage


class LoginPage(BasePage):
    # Login Page Locators
    email_address_id = "input-email"
    password_id = "input-password"
    login_button_xpath = "//input[@type='submit']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def __init__(self, driver):
        super().__init__(driver)

    def enter_credentials(self, email, password):
        self.driver.find_element(By.ID, self.email_address_id).send_keys(email)
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        return AccountPage(self.driver)

    def display_status_of_warning_message(self, expected_warning_text):
        return self.driver.find_element(By.XPATH, self.warning_message_xpath)\
            .text.__contains__(expected_warning_text)
