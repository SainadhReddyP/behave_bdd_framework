from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import random


def before_scenario(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")


def after_scenario(context):
    context.driver.quit()


@given('user navigated to Register page')
def launch_register_page(context):
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Register").click()


@when('user enter mandatory fields')
def enter_mandatory(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("Sainadh")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Reddy")
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    email_id = "sainadhreddy_" + time_stamp + "@gmail.com"
    context.driver.find_element(By.ID, "input-email").send_keys(email_id)
    telephone_number ='9' + ''.join(str(random.randint(0, 9)) for _ in range(9))
    context.driver.find_element(By.ID, "input-telephone").send_keys(telephone_number)
    context.driver.find_element(By.ID, "input-password").send_keys("123456")
    context.driver.find_element(By.ID, "input-confirm").send_keys("123456")
    context.driver.find_element(By.NAME, "agree").click()


@when('clicks on continue button')
def click_continue(context):
    context.driver.find_element(By.XPATH, "//input[@value='Continue']").click()


@then('account should get created')
def account_created(context):
    expected_result = "Your Account Has Been Created!"
    assert context.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_result)


@when('user enter all fields')
def enter_all_fields(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("Sainadh")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Reddy")
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    email_id = "sainadhreddy_" + time_stamp + "@gmail.com"
    context.driver.find_element(By.ID, "input-email").send_keys(email_id)
    telephone_number = '9' + ''.join(str(random.randint(0, 9)) for _ in range(9))
    context.driver.find_element(By.ID, "input-telephone").send_keys(telephone_number)
    context.driver.find_element(By.ID, "input-password").send_keys("123456")
    context.driver.find_element(By.ID, "input-confirm").send_keys("123456")
    context.driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()
    context.driver.find_element(By.NAME, "agree").click()


@when('user enter all fields except email field')
def enter_all_fields(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("Sainadh")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Reddy")
    telephone_number = '9' + ''.join(str(random.randint(0, 9)) for _ in range(9))
    context.driver.find_element(By.ID, "input-telephone").send_keys(telephone_number)
    context.driver.find_element(By.ID, "input-password").send_keys("123456")
    context.driver.find_element(By.ID, "input-confirm").send_keys("123456")
    context.driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()
    context.driver.find_element(By.NAME, "agree").click()


@when('user enter existing accounts email into email field')
def enter_existing_details(context):
    context.driver.find_element(By.ID, "input-email").send_keys("sainadhreddy@gmail.com")


@then('proper warning message informing about duplicate account should be displayed')
def warning_duplicate_account(context):
    expected_warning = "Warning: E-Mail Address is already registered!"
    assert context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]") \
        .text.__contains__(expected_warning)


@when('user dont enter anything into all fields')
def dont_enter_anything(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("")
    context.driver.find_element(By.ID, "input-lastname").send_keys("")
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-telephone").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
    context.driver.find_element(By.ID, "input-confirm").send_keys("")


@then('proper warning message for every mandatory fields should be displayed')
def mandatory_fields_warning_message(context):
    expected_privacy_warning = "Warning: You must agree to the Privacy Policy!"
    expected_fname_warning = "First Name must be between 1 and 32 characters!"
    expected_lname_warning = "Last Name must be between 1 and 32 characters!"
    expected_email_warning = "E-Mail Address does not appear to be valid!"
    expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
    expected_password_warning = "Password must be between 4 and 20 characters!"
    assert context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]")\
        .text.__contains__(expected_privacy_warning)

    assert context.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div") \
        .text.__contains__(expected_fname_warning)

    assert context.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div") \
        .text.__eq__(expected_fname_warning)

    assert context.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div") \
        .text.__eq__(expected_lname_warning)

    assert context.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div") \
        .text.__eq__(expected_email_warning)

    assert context.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div") \
        .text.__eq__(expected_telephone_warning)

    assert context.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div") \
        .text.__eq__(expected_password_warning)
