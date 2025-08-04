from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LinkedInLoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        self.browser.wait_for_element(By.ID, 'username').send_keys(username)
        self.browser.wait_for_element(By.ID, 'password').send_keys(password)
        print("✅ Username and password entered")

        try:
            WebDriverWait(self.browser.browser, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
            ).click()
            print("✅ Clicked login button")
        except Exception as e:
            print("❌ Could not click login button:", e)
            raise
