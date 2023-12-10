from selenium import webdriver


def before_scenario(context, driver):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")


def after_scenario(context, driver):
    context.driver.quit()