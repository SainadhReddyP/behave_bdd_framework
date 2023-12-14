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
        self.set_text("email_address_id", self.email_address_id, email)
        self.set_text("password_id", self.password_id, password)

    def click_on_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        return AccountPage(self.driver)

    def display_status_of_warning_message(self, expected_warning_text):
        return self.retrieved_element_text_contains("warning_message_xpath", self.warning_message_xpath, expected_warning_text)