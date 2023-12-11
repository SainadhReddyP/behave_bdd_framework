from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class SearchPage(BasePage):
    # Search Page Locators
    hp_product_link_txt = "HP LP3065"
    msg_xpath = "//input[@id='button-search']/following-sibling::p"

    def __init__(self, driver):
        super().__init__(driver)

    def display_status_of_product(self):
        return self.driver.find_element(By.LINK_TEXT, self.hp_product_link_txt).is_displayed()

    def display_status_of_search_results(self, expected_text):
        return self.driver.find_element(By.XPATH, self.msg_xpath).text.__eq__(expected_text)
