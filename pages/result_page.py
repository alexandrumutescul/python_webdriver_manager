"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By

class DuckDuckGoResultPage:
    
    # Locators
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT_FIELD = (By.ID, 'search_form_input')
    
    # Initializer
    def __init__(self, driver):
        self.driver = driver
        
    # Interaction methods
    def result_link_titles(self):
        links = self.driver.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles
    
    def search_input_value(self):
        search_input_field = self.driver.find_element(*self.SEARCH_INPUT_FIELD)
        value = search_input_field.get_attribute('value')
        return value
    
    def title(self):
        return self.driver.title