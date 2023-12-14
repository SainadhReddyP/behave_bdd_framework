from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class RegisterPage(BasePage):
    # Register Page Locators
    fname_id = "input-firstname"
    lname_id = "input-lastname"
    email_id = "input-email"
    telephone_id = "input-telephone"
    password_id = "input-password"
    password_confirm_id = "input-confirm"
    policy_agree_name = "agree"
    continue_btn_xpath = "//input[@value='Continue']"
    account_created_msg_xpath = "//div[@id='content']/h1"
    news_letter_xpath = "//input[@name='newsletter' and @value='1']"
    duplicate_email_msg_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath = "//input[@id='input-password']/following-sibling::div"

    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name_txt):
        self.set_text("fname_id", self.fname_id, first_name_txt)

    def enter_last_name(self, last_name_txt):
        self.set_text("lname_id", self.lname_id, last_name_txt)

    def enter_email(self, email_txt):
        self.set_text("email_id", self.email_id, email_txt)

    def enter_telephone(self, telephone_number):
        self.set_text("telephone_id", self.telephone_id, telephone_number)

    def enter_password(self, password):
        self.set_text("password_id", self.password_id, password)

    def enter_confirm_password(self, confirm_password):
        self.set_text("password_confirm_id", self.password_confirm_id, confirm_password)

    def select_privacy_policy(self):
        self.click_on_element("policy_agree_name", self.policy_agree_name)

    def clicks_on_continue_button(self):
        self.click_on_element("continue_btn_xpath", self.continue_btn_xpath)

    def status_msg_account_created(self, expected_result_msg_txt):
        return self.retrieved_element_text_equals("account_created_msg_xpath", self.account_created_msg_xpath, expected_result_msg_txt)

    def select_news_letter(self):
        self.click_on_element("news_letter_xpath", self.news_letter_xpath)

    def duplicate_email_warning(self, expected_warning_text):
        return self.retrieved_element_text_contains("duplicate_email_msg_xpath", self.duplicate_email_msg_xpath, expected_warning_text)

    def privacy_policy_warning(self, expected_warning_text):
        return self.retrieved_element_text_contains("privacy_policy_warning_xpath", self.privacy_policy_warning_xpath, expected_warning_text)

    def display_status_of_warnings(self, fname_warning, lname_warning, email_warning, tel_warning, pwd_warning):
        fname_status = self.retrieved_element_text_equals("first_name_warning_xpath", self.first_name_warning_xpath, fname_warning)
        lname_status = self.retrieved_element_text_equals("last_name_warning_xpath", self.last_name_warning_xpath, lname_warning)
        email_status = self.retrieved_element_text_equals("email_warning_xpath", self.email_warning_xpath, email_warning)
        tel_status = self.retrieved_element_text_equals("telephone_warning_xpath", self.telephone_warning_xpath, tel_warning)
        pwd_status = self.retrieved_element_text_equals("password_warning_xpath", self.password_warning_xpath, pwd_warning)

        return fname_status, lname_status, email_status, tel_status, pwd_status



