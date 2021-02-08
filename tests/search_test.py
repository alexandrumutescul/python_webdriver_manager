"""
These tests cover DuckDuckGo searches.
"""

from pages.result_page import DuckDuckGoResultPage
from pages.search_page import DuckDuckGoSearchPage


def test_basic_duckduckgo_search(driver):
    
    PHRASE = "panda"   
    HOME_PAGE_URL = 'https://www.duckduckgo.com'
    
    search_page = DuckDuckGoSearchPage(driver)
    result_page = DuckDuckGoResultPage(driver)
    
    # Given the DuckDuckGo home page is displayed
    search_page.go_to_url(HOME_PAGE_URL)
    
    # When the user searched for "panda"
    search_page.search(PHRASE)
    
    # Then the search result title contains "panda"
    assert PHRASE in result_page.title()
    
    # And the search result query is "panda"
    assert PHRASE == result_page.search_input_value()
    
    # And the search result link pertain to "panda"
    for title in result_page.result_link_titles():
        assert PHRASE.lower() in title.lower()
    
    