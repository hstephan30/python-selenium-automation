from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target.com')
def open_target(context):
    context.driver.get('https://target.com/')


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]').click()


@then('Verify "Your Cart is empty" message is shown')
def verify_cart_is_empty(context):
    sleep(5)
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, 'h1').text
    assert expected_text == actual_text, f'Expected:{expected_text} but got {actual_text}'
