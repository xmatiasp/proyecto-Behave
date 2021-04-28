from selenium.webdriver.common.by import By

class IndexPage:

    def __init__(self, driver):
        self.driver = driver
        self.dresses_button = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a')
        self.search_input =(By.ID, 'search_query_top')
        self.search_button = (By.NAME, 'submit_search')

    def click_dresses(self):
        self.driver.find_element(*self.dresses_button).click()

    def search_item(self, item):
        self.driver.find_element(*self.search_input).send_keys(item)
        self.driver.find_element(*self.search_button).click()
