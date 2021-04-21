from behave import *
from selenium import webdriver
from nose.tools import assert_equal

@given('the user is in the main page')
def step_impl(context):
    context.browser = webdriver.Chrome('./drivers/chromedriver.exe')
    context.browser.implicitly_wait(10)
    context.browser.get('http://automationpractice.com/index.php')

@when('the user clicks on the dresses button')
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[2]/a').click()

@then('the user should see dresses page')
def step_impl(context):
    assert_equal(context.browser.find_element_by_class_name('cat-name').text, 'DRESSES ')
    