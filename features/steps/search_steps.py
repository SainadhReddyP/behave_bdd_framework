from behave import given, when, then
from selenium.webdriver.common.by import By


@given('user navigated to Home page')
def home_page(context):
    expected_title = "Your Store"
    assert context.driver.title.__eq__(expected_title)


@when('user enter valid product into the search box')
def valid_search(context):
    context.driver.find_element(By.NAME, "search").send_keys("HP")


@when('user clicks on search button')
def click_search(context):
    context.driver.find_element(By.XPATH, "//div[@id='search']//button").click()


@then('valid product should get displayed in search results')
def valid_search_result(context):
    assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()


@when('user enter invalid product into the search box')
def invalid_search(context):
    context.driver.find_element(By.NAME, "search").send_keys("DELL")


@then('proper message should be displayed in search results')
def message_invalid_search(context):
    expected_text = "There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p")\
        .text.__eq__(expected_text)


@when('user dont enter anything into search box')
def empty_search(context):
    context.driver.find_element(By.NAME, "search").send_keys("")
