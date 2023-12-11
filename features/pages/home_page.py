from selenium.webdriver.common.by import By
from features.pages.search_page import SearchPage
from features.pages.login_page import LoginPage
from features.pages.register_page import RegisterPage
from features.pages.base_page import BasePage


class HomePage(BasePage):
    # Home Page Locators
    my_account_xpath = "//span[text()='My Account']"
    login_link_text = "Login"
    search_box_name = "search"
    search_btn_xpath = "//div[@id='search']//button"
    register_link_text = "Register"

    def __init__(self, driver):
        super().__init__(driver)

    def click_my_account(self):
        self.click_on_element("my_account_xpath", self.my_account_xpath)

    def select_login(self):
        self.click_on_element("login_link_text", self.login_link_text)
        return LoginPage(self.driver)

    def verify_home_page_title(self, expected_title_text):
        return self.driver.title.__eq__(expected_title_text)

    def enter_product_into_search_box(self, product_text):
        self.driver.find_element(By.NAME, self.search_box_name).send_keys(product_text)

    def clicks_on_search(self):
        self.click_on_element("search_btn_xpath", self.search_btn_xpath)
        return SearchPage(self.driver)

    def select_register(self):
        self.click_on_element("register_link_text", self.register_link_text)
        return RegisterPage(self.driver)