import sys
import os


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from browser_wrapper import Browser

import pytest

@pytest.fixture
def browser():
    driver_path = r"C:\web\chromedriver.exe"
    browser = Browser(driver_path, headless=False)
    yield browser
    browser.close_browser()
