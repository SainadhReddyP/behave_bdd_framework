from behave import given, when, then
from selenium.webdriver.common.by import By
from datetime import datetime
import random


@given('user navigated to Login page')
def login_page(context):
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Login").click()


@when('user entered valid credentials')
def enter_valid_credentials(context):
    context.driver.find_element(By.ID, "input-email").send_keys("sainadhreddy@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("sainadh@123")


@when('clicks on Login button')
def click_login(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()


@then('user should get logged in')
def successful_login(context):
    assert context.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()


@when('user entered invalid credentials')
def invalid_credentials(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "sainadhreddy_" + time_stamp + "@gmail.com"
    context.driver.find_element(By.ID, "input-email").send_keys(invalid_email)
    invalid_password = ''.join(str(random.randint(0, 9)) for i in range(8))
    context.driver.find_element(By.ID, "input-password").send_keys(invalid_password)


@then('user should get a proper warning message')
def warning_message(context):
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert context.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").\
        text.__contains__(expected_warning_message)


@when('user enter valid email and invalid password')
def valid_email_invalid_password(context):
    context.driver.find_element(By.ID, "input-email").send_keys("sainadhreddy@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("12345")


@when('user enter invalid email and valid password')
def invalid_email_valid_password(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "sainadhreddy_" + time_stamp + "_@gmail.com"
    context.driver.find_element(By.ID, "input-email").send_keys(invalid_email)
    context.driver.find_element(By.ID, "input-password").send_keys("12345")


@when('user dont enter anything in email and password fields')
def without_entering_credentials(context):
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
