from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    my_account_xpath = "//span[text()='My Account']"

    def click_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()