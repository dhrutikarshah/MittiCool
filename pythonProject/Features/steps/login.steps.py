from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('User is on the signin page')
def launch_login_page(context):
    print("Launch login page")
    context.driver = webdriver.Chrome()
    context.driver.get('https://mitticool.com/my-account/')


@when('User enters valid username and password')
def validate_user_credentials(context):
    print("Submit login username and password")
    username = "dhrutikarshah@gmail.com"
    password = "india123"
    context.driver.find_element(By.ID, "username").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.NAME, "login").click()


@then('User will be able to navigate to homepage')
def validate_login(context):
    print("Validate successful login")
    elem = context.driver.find_element(By.XPATH, "//div[@class='inner-block']//a[normalize-space()='My Account']")
    status = elem.is_displayed()
    assert status is True
