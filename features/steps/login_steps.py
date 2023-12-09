from behave import given, when, then

@given('user navigated to Login page')
def step_impl(context):
    pass


@when('user entered valid credentials')
def step_impl(context):
    pass


@when('clicks on Login button')
def step_impl(context):
    pass


@then('user should get logged in')
def step_impl(context):
    pass


@when('user entered invalid credentials')
def step_impl(context):
    pass


@then('user should get a proper warning message')
def step_impl(context):
    pass


@when('user enter valid email and invalid password')
def step_impl(context):
    pass


@when('user enter invalid email and valid password')
def step_impl(context):
    pass


@when('user dont enter anything in email and password fields')
def step_impl(context):
    pass
