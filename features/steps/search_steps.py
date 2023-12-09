from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('user navigated to Home page')
def home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")


@when('user enter valid product into the search box')
def valid_search(context):
    context.driver.find_element(By.NAME, "search").send_keys("HP")


@when('user clicks on search button')
def click_search(context):
    context.driver.find_element(By.XPATH, "//div[@id='search']//button").click()


@then('valid product should get displayed in search results')
def valid_search_result(context):
    assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    context.driver.quit()


@when('user enter invalid product into the search box')
def invalid_search(context):
    context.driver.find_element(By.NAME, "search").send_keys("DELL")


@then('proper message should be displayed in search results')
def message_invalid_search(context):
    expected_text = "There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p")\
        .text.__eq__(expected_text)
    context.driver.quit()


@when('user dont enter anything into search box')
def empty_search(context):
    context.driver.find_element(By.NAME, "search").send_keys("")
