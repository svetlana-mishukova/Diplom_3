import os
import sys
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import TimeoutException 
from pages.basic_functionality_page import BasicFunctionalityPage
from pages.order_feed_page import OrderFeedPage
from pages.base_page import BasePage

from curl import *


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-extensions")  
        chrome_options.add_argument("--disable-gpu") 
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1920,1080")
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(main_site)
        
    elif request.param == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--disable-extensions")  
        firefox_options.add_argument("--disable-gpu") 
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--window-size=1920,1080")

        driver = webdriver.Firefox(options=firefox_options)
        driver.get(main_site)
        driver.implicitly_wait(60)
    yield driver
    driver.quit()
    