from behave import given, when, then


@given('user navigated to Register page')
def step_impl(context):
    print('Given user navigated to Register page')


@when('user enter mandatory fields')
def step_impl(context):
    print('When user enter mandatory fields')


@when('clicks on continue button')
def step_impl(context):
    print('When clicks on continue button')


@then('account should get created')
def step_impl(context):
    print('Then account should get created')


@when('user enter all fields')
def step_impl(context):
    print('When user enter all fields')


@when('user enter all fields except email field')
def step_impl(context):
    print('When user enter all fields except email field')


@when('user enter existing accounts email into email field')
def step_impl(context):
    print('When user enter existing accounts email into email field')


@then('proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    print('Then proper warning message informing about duplicate account should be displayed')


@when('user dont enter anything into all fields')
def step_impl(context):
    print('When user dont enter anything into all fields')


@then('proper warning message for every mandatory fields should be displayed')
def step_impl(context):
    print('Then proper warning message for every mandatory fields should be displayed')
