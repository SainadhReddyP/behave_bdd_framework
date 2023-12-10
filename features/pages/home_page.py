from selenium.webdriver.common.by import By


class HomePage:
    # Home Page Locators
    my_account_xpath = "//span[text()='My Account']"
    login_link_text = "Login"
    search_box_name = "search"
    search_btn_xpath = "//div[@id='search']//button"

    def __init__(self, driver):
        self.driver = driver

    def click_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def select_login(self):
        self.driver.find_element(By.LINK_TEXT, self.login_link_text).click()

    def verify_home_page_title(self, expected_title_text):
        return self.driver.title.__eq__(expected_title_text)

    def enter_product_into_search_box(self, product_text):
        self.driver.find_element(By.NAME, self.search_box_name).send_keys(product_text)

    def clicks_on_search(self):
        self.driver.find_element(By.XPATH, self.search_btn_xpath).click()

