import os
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from linkedin_page import LinkedInLoginPage

def test_login_linkedin_success(browser):
    browser.open_page("https://www.linkedin.com/login")
    time.sleep(2)
    page = LinkedInLoginPage(browser)
    page.login("pythonautomation1267@gmail.com", "Pytest12@!")

    WebDriverWait(browser.browser, 30).until(EC.title_contains("Feed"))
    assert "Feed" in browser.browser.title

    folder = r"C:\Users\ASG42\OneDrive\Pictures\scs"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(folder, f"linkedin_success_{timestamp}.png")
    browser.browser.save_screenshot(path)

def test_login_linkedin_invalid(browser):
    browser.open_page("https://www.linkedin.com/login")
    time.sleep(2)
    page = LinkedInLoginPage(browser)
    page.login("wrong.email@example.com", "wrongPass123")

    error_xpath = '//*[@id="error-for-password"]'
    error_displayed = browser.wait_for_element(By.XPATH, error_xpath)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(
        r"C:\Users\ASG42\OneDrive\Pictures\scs", f"error_debug_{timestamp}.png"
    )
    browser.browser.save_screenshot(screenshot_path)

    assert error_displayed.is_displayed()
