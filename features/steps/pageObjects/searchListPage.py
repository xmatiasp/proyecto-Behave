from selenium.webdriver.common.by import By

class SearchListPage:

    def __init__(self, driver):
        self.driver = driver
        self.banner_text = (By.CLASS_NAME, 'lighter')

    def get_banner_text(self):
        return self.driver.find_element(*self.banner_text).text
