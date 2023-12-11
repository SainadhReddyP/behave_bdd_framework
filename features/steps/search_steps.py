from behave import given, when, then
from features.pages.home_page import HomePage
from features.pages.search_page import SearchPage


@given('user navigated to Home page')
def home_page(context):
    context.home_pg = HomePage(context.driver)
    expected_title = "Your Store"
    assert context.home_pg.verify_home_page_title(expected_title)


@when('user enter valid product into the search box')
def valid_search(context):
    context.home_pg.enter_product_into_search_box("HP")


@when('user clicks on search button')
def click_search(context):
    context.search_pg = context.home_pg.clicks_on_search()


@then('valid product should get displayed in search results')
def valid_search_result(context):
    assert context.search_pg.display_status_of_product()


@when('user enter invalid product into the search box')
def invalid_search(context):
    context.home_pg.enter_product_into_search_box("DELL")


@then('proper message should be displayed in search results')
def message_invalid_search(context):
    expected_msg_text = "There is no product that matches the search criteria."
    assert context.search_pg.display_status_of_search_results(expected_msg_text)


@when('user dont enter anything into search box')
def empty_search(context):
    context.home_pg.enter_product_into_search_box("")
