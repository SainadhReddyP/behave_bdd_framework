from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class AccountPage(BasePage):
    # Account Page Locators
    edit_account_information_link_txt = "Edit your account information"

    def __init__(self, driver):
        super().__init__(driver)

    def display_status_of_edit_your_account_information(self):
        return self.driver.find_element(By.LINK_TEXT, self.edit_account_information_link_txt).is_displayed()
