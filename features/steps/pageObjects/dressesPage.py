from selenium.webdriver.common.by import By

class DressesPage:
    def __init__(self, driver):
        self.driver = driver
        self.category_name = (By.CLASS_NAME, 'cat-name')

    def get_category_name(self):
        return self.driver.find_element(*self.category_name).text
