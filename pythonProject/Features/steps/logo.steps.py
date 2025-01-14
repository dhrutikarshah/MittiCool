from behave import given, when, then
from selenium import webdriver

from selenium.webdriver.common.by import By

@given('Launch web browser')
def launch_browser(context):
    print("Launch Chrome browser")
    context.driver = webdriver.Chrome()

@when('View mitticool home page')
def open_home_page(context):
    print("Navigate to mitticool homepage")
    context.driver.get('https://www.mitticool.com/')

@then('Check logo is present on homepage')
def verify_logo(context):
    print("Validate logo is displayed on the homepage")
    elem = context.driver.find_element(By.XPATH, "//h1[@class='nasa-logo-img']//img[@alt='Mitticool']")
    status = elem.is_displayed()
    assert status is True

@then('Close browser')
def close_browser(context):
    print("Close Chrome browser")
    context.driver.close()

