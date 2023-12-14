from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class SearchPage(BasePage):
    # Search Page Locators
    hp_product_link_text = "HP LP3065"
    msg_xpath = "//input[@id='button-search']/following-sibling::p"

    def __init__(self, driver):
        super().__init__(driver)

    def display_status_of_product(self):
        return self.display_status("hp_product_link_text", self.hp_product_link_text)

    def display_status_of_search_results(self, expected_text):
        return self.retrieved_element_text_equals("msg_xpath", self.msg_xpath, expected_text)
