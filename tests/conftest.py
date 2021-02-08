"""
This module contains shared fixtures.
"""

import json
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def config(scope='session'):
    
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)
        
    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    
    # Return config so it can be used
    return config

@pytest.fixture
def driver(config):
    
    # Initialize the WebDriver instance
    #driver = selenium.webdriver.Chrome()
    
    if config['browser'] == 'Chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif config['browser'] == 'Headless Chrome':
        opts = webdriver.ChromeOptions(ChromeDriverManager().install())
        opts.add_argument('headless')
        driver = webdriver.Chrome(options=opts)
    elif config['browser'] == 'Firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else: 
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    
    driver.maximize_window()
    
    #resources executable_path=r"C:\Users\alexandru.mutescul\python_projects\ui_ta\tau-intro-selenium-py\resources\chromedriver.exe"
    
    # Make its calls wait up to 10 seconds for elements to appear
    driver.implicitly_wait(config['implicit_wait'])
    
    # Return the WebDriver instace for the setup
    yield driver
    
    # Quit the WebDriver instance for the cleanup
    driver.quit()
