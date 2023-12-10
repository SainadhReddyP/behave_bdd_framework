from selenium.webdriver.common.by import By


class HomePage:
    # Home Page Locators
    my_account_xpath = "//span[text()='My Account']"
    login_link_text = "Login"

    def __init__(self, driver):
        self.driver = driver

    def click_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def select_login(self):
        self.driver.find_element(By.LINK_TEXT, self.login_link_text).click()