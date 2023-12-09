from behave import given, when, then


@given('user navigated to Home page')
def step_impl(context):
    pass


@when('user enter valid product into the search box')
def step_impl(context):
    pass


@when('user clicks on search button')
def step_impl(context):
    pass


@when('user dont enter anything into search box')
def step_impl(context):
    pass


@then('valid product should get displayed in search results')
def step_impl(context):
    pass


@when('user enter invalid product into the search box')
def step_impl(context):
    pass


@then('proper message should be displayed in search results')
def step_impl(context):
    pass
