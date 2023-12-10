from selenium.webdriver.common.by import By


class RegisterPage:
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

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name_txt):
        self.driver.find_element(By.ID, self.fname_id).send_keys(first_name_txt)

    def enter_last_name(self, last_name_txt):
        self.driver.find_element(By.ID, self.lname_id).send_keys(last_name_txt)

    def enter_email(self, email_txt):
        self.driver.find_element(By.ID, self.email_id).send_keys(email_txt)

    def enter_telephone(self, telephone_number):
        self.driver.find_element(By.ID, self.telephone_id).send_keys(telephone_number)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.ID, self.password_confirm_id).send_keys(confirm_password)

    def select_privacy_policy(self):
        self.driver.find_element(By.NAME, self.policy_agree_name).click()

    def clicks_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_btn_xpath).click()

    def status_msg_account_created(self, expected_result_msg_txt):
        self.driver.find_element(By.XPATH, self.account_created_msg_xpath)\
            .text.__eq__(expected_result_msg_txt)

    def select_news_letter(self):
        self.driver.find_element(By.XPATH, self.news_letter_xpath).click()

    def duplicate_email_warning(self, expected_warning_text):
        return self.driver.find_element(By.XPATH, self.duplicate_email_msg_xpath) \
            .text.__contains__(expected_warning_text)

    def mandatory_fiels_warning_msgs(self):