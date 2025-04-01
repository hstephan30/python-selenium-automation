from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target.com')
def open_target(context):
    context.driver.get('https://target.com/')

    @when('Click on cart icon')
    def click_sign_in_icon(context):
        context.driver.find_element(By.CSS_SELECTOR,'a[aria-label="Account, sign in"]').click()

        @then('Verify "sing in formed opened')
        def verify_sign_in(context):
            sleep(5)
            expected_text = ('sign in formed opened')
            actual_text = context.driver.find_element(By.CSS_SELECTOR, 'h1').text
            assert expected_text == actual_text, f'Expected:{expected_text} but got {actual_text}'