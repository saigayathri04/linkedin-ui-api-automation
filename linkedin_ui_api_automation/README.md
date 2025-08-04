# 🤖 LinkedIn UI + API Automation using Selenium, PyTest, and Requests

This project automates the login process of LinkedIn using Selenium WebDriver and validates a public REST API using the `requests` library. The entire suite is managed using the `pytest` framework with HTML reporting support.

---

## 📌 Features

- ✅ LinkedIn UI login automation (Valid and Invalid credentials)
- ✅ API test using [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/)
- ✅ Screenshot capture for both success and failure scenarios
- ✅ PyTest framework with fixtures for clean test management
- ✅ Generates beautiful HTML test reports (`pytest-html`)

---

## 🧪 Tech Stack

| Layer       | Tool/Library               |
|-------------|----------------------------|
| UI Testing  | Selenium WebDriver         |
| API Testing | Python `requests`          |
| Test Runner | PyTest                     |
| Reporting   | PyTest-HTML                |
| Language    | Python 3                   |

---

## 🗂 Project Structure

linkedin_ui_api_automation/
│
├── browser_wrapper.py # Selenium browser wrapper
├── linkedin_page.py # LinkedIn Page Object
├── conftest.py # PyTest fixture for browser setup
├── test_linkedin.py # UI tests (valid/invalid login)
├── test_api.py # REST API validation
├── requirements.txt # Python dependencies
├── report.html # HTML report (generated)


## How to Run the Tests

### 🔹 Step 1: Install Dependencies
pip install -r requirements.txt
🔹 Step 2: Run All Tests + Generate HTML Report
bash
Copy
Edit
pytest --html=report.html

📸 Screenshots
Screenshots are auto-saved to the specified folder:
C:\Users\ASG42\OneDrive\Pictures\scs
🎯 Test Cases
Test Case	Description
test_login_linkedin_success	Valid LinkedIn login with screenshot
test_login_linkedin_invalid	Invalid login + error message check
test_public_api_status	Validates REST API response

