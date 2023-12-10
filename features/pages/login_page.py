from selenium.webdriver.common.by import By


class LoginPage:
    # Login Page Locators
    email_address_id = "input-email"
    password_id = "input-password"
    login_button_xpath = "//input[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def enter_credentials(self, email, password):
        self.driver.find_element(By.ID, self.email_address_id).send_keys(email)
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
