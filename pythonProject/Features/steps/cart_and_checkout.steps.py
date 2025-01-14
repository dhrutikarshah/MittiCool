from time import sleep

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('User is on the product listing page')
def launch_product_listing_page(context):
    print("User is on the product listing page")
    context.driver = webdriver.Chrome()
    context.driver.get('https://mitticool.com/shop/')


@when('User selects a product')
def select_product(context):
    print("User selects a product")
    product_elem = context.driver.find_element(By.XPATH, "//a[normalize-space()='Clay Cooker 3 Liters']")
    product_elem.click()
    print("Navigating to product page")
    sleep(3)
    add_to_cart_elem = context.driver.find_element(By.NAME, "add-to-cart")
    status = add_to_cart_elem.is_displayed()
    assert status is True

@when('User clicks add to cart button')
def add_product_to_cart(context):
    print("User clicks Add to Cart button")
    add_to_cart_elem = context.driver.find_element(By.NAME, "add-to-cart")
    add_to_cart_elem.click()


@then('Cart should display the selected product')
def view_product_on_cart(context):
    print("Validate product on Cart")
    sleep(6)
    context.driver.get('https://mitticool.com/shopping-cart/')
    cart_elem = context.driver.find_element(By.XPATH, "//td[@class='product-name']//a[contains(text(),'Clay Cooker 3 Liters')]")
    status = cart_elem.is_displayed()
    assert status is True
    print("Validate proceed to checkout")
    checkout_elem = context.driver.find_element(By.XPATH, "//a[normalize-space()='Proceed to checkout']")
    status = checkout_elem.is_displayed()
    assert status is True

@then('User clicks proceed to checkout')
def view_product_on_cart(context):
    print("User clicks proceed to checkout")
    checkout_elem = context.driver.find_element(By.XPATH, "//a[normalize-space()='Proceed to checkout']")
    checkout_elem.click()
    sleep(3)
    print('validate user is on checkout page')
    billing_elem = context.driver.find_element(By.XPATH, "//h3[normalize-space()='Billing & Shipping']")
    status = billing_elem.is_displayed()
    assert status is True

@then('Place order on checkout page')
def checkout_page(context):
    print("User is on checkout page")
    context.driver.find_element(By.ID, "billing_first_name").send_keys("Dhrutika")
    context.driver.find_element(By.ID, "billing_last_name").send_keys("Parekh")
    context.driver.find_element(By.ID, "billing_address_1").send_keys("2816 Saint Paul Rivera")
    context.driver.find_element(By.ID, "billing_city").send_keys("Alibag")
    context.driver.find_element(By.ID, "billing_postcode").send_keys("402201")
    stateElem = context.driver.find_element(By.XPATH, "//span[ @ id = 'select2-billing_state-container']")
    context.driver.execute_script("arguments[0].innerText = 'Maharashtra'", stateElem)
    context.driver.find_element(By.ID, "billing_phone").send_keys("9821888888")
    context.driver.find_element(By.ID, "billing_email").send_keys("dhrutikarshah@gmail.com")
    context.driver.find_element(By.ID, "terms").click()
    context.driver.find_element(By.ID, "place_order").click()
    print("Order placed navigating to the payment processor")
    sleep(20)