"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from pages.result_page import DuckDuckGoResultPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:
    
    # URL
    
    # URL = 'https://www.duckduckgo.com'
    
    # Locators
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    # S_INPUT = By.ID('search_form_input_homepage')
    
    # Initializer
    def __init__(self, driver):
        self.driver = driver
        
    # Interaction methods
        
    def go_to_url(self, url):
        self.driver.get(url)
    
    def search(self, phrase):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
    
    def returnResult(self, driver):
        DuckDuckGoResultPage(driver)