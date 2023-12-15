from selenium import webdriver
from utilities import ConfigReader
import allure
from allure_commons.types import AttachmentType


def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic_info", "browser")
    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic_info", "url"))


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(),
                      name=step.name, attachment_type=AttachmentType.PNG)