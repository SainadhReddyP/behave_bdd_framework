from selenium.webdriver.common.by import By


class AccountPage:
    # Account Page Locators
    edit_account_information_link_txt = "Edit your account information"

    def __init__(self, driver):
        self.driver = driver

    def display_status_of_edit_your_account_information(self):
        return self.driver.find_element(By.LINK_TEXT, self.edit_account_information_link_txt).is_displayed()
