from behave import given, when, then
from datetime import datetime
from features.pages.home_page import HomePage
from features.pages.login_page import LoginPage
from features.pages.account_page import AccountPage
import random


@given('user navigated to Login page')
def login_page(context):
    context.home_pg = HomePage(context.driver)
    context.home_pg.click_my_account()
    context.home_pg.select_login()


@when('user entered valid credentials')
def enter_valid_credentials(context):
    context.login_pg = LoginPage(context.driver)
    context.login_pg.enter_credentials("sainadhreddy@gmail.com","sainadh@123")


@when('clicks on Login button')
def click_login(context):
    context.login_pg.click_on_login_button()


@then('user should get logged in')
def successful_login(context):
    account_pg = AccountPage(context.driver)
    assert account_pg.display_status_of_edit_your_account_information()


@when('user entered invalid credentials')
def invalid_credentials(context):
    context.login_pg = LoginPage(context.driver)
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "sainadhreddy_" + time_stamp + "@gmail.com"
    invalid_password = ''.join(str(random.randint(0, 9)) for i in range(8))
    context.login_pg.enter_credentials(invalid_email, invalid_password)


@then('user should get a proper warning message')
def warning_message(context):
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert context.login_pg.display_status_of_warning_message(expected_warning_message)


@when('user enter valid email and invalid password')
def valid_email_invalid_password(context):
    context.login_pg = LoginPage(context.driver)
    context.login_pg.enter_credentials("sainadhreddy@gmail.com", "123")


@when('user enter invalid email and valid password')
def invalid_email_valid_password(context):
    context.login_pg = LoginPage(context.driver)
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "sainadhreddy_" + time_stamp + "_@gmail.com"
    context.login_pg.enter_credentials(invalid_email, "123456")


@when('user dont enter anything in email and password fields')
def without_entering_credentials(context):
    context.login_pg = LoginPage(context.driver)
    context.login_pg.enter_credentials("","")
