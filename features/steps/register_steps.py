from behave import given, when, then
from selenium.webdriver.common.by import By
from datetime import datetime
from features.pages.home_page import HomePage
from features.pages.register_page import RegisterPage
from configurations.app_config import AppConfig
import random


@given('user navigated to Register page')
def launch_register_page(context):
    context.home_pg = HomePage(context.driver)
    context.home_pg.click_my_account()
    context.home_pg.select_register()


@when('user enter mandatory fields')
def enter_mandatory(context):
    context.register_pg = RegisterPage(context.driver)
    context.register_pg.enter_first_name(AppConfig.first_name)
    context.register_pg.enter_last_name(AppConfig.last_name)
    context.register_pg.enter_email(AppConfig.random_email_id)
    context.register_pg.enter_telephone(AppConfig.random_telephone_number)
    context.register_pg.enter_password(AppConfig.password)
    context.register_pg.enter_confirm_password(AppConfig.password)
    context.register_pg.select_privacy_policy()


@when('clicks on continue button')
def click_continue(context):
    context.register_pg.clicks_on_continue_button()


@then('account should get created')
def account_created(context):
    expected_result = "Your Account Has Been Created!"
    assert context.register_pg.status_msg_account_created(expected_result)


@when('user enter all fields')
def enter_all_fields(context):
    context.register_pg = RegisterPage(context.driver)
    context.register_pg.enter_first_name(AppConfig.first_name)
    context.register_pg.enter_last_name(AppConfig.last_name)
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    random_email_id = "sainadhreddy_" + time_stamp + "@gmail.com"
    context.register_pg.enter_email(random_email_id)
    context.register_pg.enter_telephone(AppConfig.random_telephone_number)
    context.register_pg.enter_password(AppConfig.password)
    context.register_pg.enter_confirm_password(AppConfig.password)
    context.register_pg.clicks_on_continue_button()
    context.register_pg.select_news_letter()
    context.register_pg.select_privacy_policy()


@when('user enter all fields except email field')
def enter_all_fields_except_email(context):
    context.register_pg = RegisterPage(context.driver)
    context.register_pg.enter_first_name(AppConfig.first_name)
    context.register_pg.enter_last_name(AppConfig.last_name)
    context.register_pg.enter_telephone(AppConfig.random_telephone_number)
    context.register_pg.enter_password(AppConfig.password)
    context.register_pg.enter_confirm_password(AppConfig.password)
    context.register_pg.select_news_letter()
    context.register_pg.select_privacy_policy()


@when('user enter existing accounts email into email field')
def enter_existing_details(context):
    context.register_pg.enter_email(AppConfig.email_id)


@then('proper warning message informing about duplicate account should be displayed')
def warning_duplicate_account(context):
    expected_warning = "Warning: E-Mail Address is already registered!"
    assert context.register_pg.duplicate_email_warning(expected_warning)


@when('user dont enter anything into all fields')
def dont_enter_anything(context):
    context.register_pg = RegisterPage(context.driver)
    context.register_pg.enter_first_name("")
    context.register_pg.enter_last_name("")
    context.register_pg.enter_email("")
    context.register_pg.enter_telephone("")
    context.register_pg.enter_password("")
    context.register_pg.enter_confirm_password("")


@then('proper warning message for every mandatory fields should be displayed')
def mandatory_fields_warning_message(context):
    expected_privacy_warning = "Warning: You must agree to the Privacy Policy!"
    expected_fname_warning = "First Name must be between 1 and 32 characters!"
    expected_lname_warning = "Last Name must be between 1 and 32 characters!"
    expected_email_warning = "E-Mail Address does not appear to be valid!"
    expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
    expected_password_warning = "Password must be between 4 and 20 characters!"

    assert context.register_pg.privacy_policy_warning(expected_privacy_warning)
    assert context.register_pg.display_status_of_warnings(expected_fname_warning, expected_lname_warning,
                                                          expected_email_warning, expected_telephone_warning,
                                                          expected_password_warning)

