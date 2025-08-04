from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser:
    def __init__(self, driver_path: str, headless=True):
        options = Options()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
        self.service = Service(driver_path)
        self.browser = webdriver.Chrome(service=self.service, options=options)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.quit()

    def wait_for_element(self, by: By, value: str, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((by, value))
        )