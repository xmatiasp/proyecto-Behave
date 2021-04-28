from behave import *
from selenium import webdriver
from nose.tools import assert_equal,assert_true
from pageObjects.indexPage import IndexPage
from pageObjects.dressesPage import DressesPage
from pageObjects.searchListPage import SearchListPage

@given('the user is in the main page')
def step_impl(context):
    context.browser = webdriver.Chrome('./drivers/chromedriver.exe')
    context.browser.implicitly_wait(10)
    context.browser.get('http://automationpractice.com/index.php')

@when('the user clicks on the dresses button')
def step_impl(context):
    indexPage = IndexPage(context.browser)
    indexPage.click_dresses()

@then('the user should see dresses page')
def step_impl(context):
    dresses = DressesPage(context.browser)
    assert_equal(dresses.get_category_name(), 'DRESSES ')

@when('the user searches by "{item}"')
def step_impl(context,item):
    indexPage = IndexPage(context.browser)
    indexPage.search_item(item)

@then('the user should sees "{item}" banner in the results')
def step_impl(context,item):
    searchList = SearchListPage(context.browser)
    assert_true(item.upper() in searchList.get_banner_text())
