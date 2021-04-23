
from behave import *

def after_scenario(context,scenario):
    context.browser.close()
    context.browser.quit()

def after_all(context):
    print("SE TERMINO")
