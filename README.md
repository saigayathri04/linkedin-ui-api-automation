# LinkedIn Login Automation Suite – UI + API Testing

This project combines Selenium-based UI automation and API validation using Python's `requests` module. Tests are structured using PyTest, focusing on LinkedIn login functionality across both frontend and backend layers. HTML reports are generated with `pytest-html` for easy result visualization.

---

## ⚙️ Tech Stack Overview

| Tool           | Purpose                                |
|----------------|----------------------------------------|
| Python         | Scripting language                     |
| Selenium       | Automates LinkedIn login via web UI    |
| PyTest         | Framework for organizing test cases    |
| Requests       | Used for REST API validation           |
| pytest-html    | Generates HTML test reports            |
| Git & GitHub   | Version control and hosting            |
| PyCharm        | Development environment                |

---

## 📁 Project Structure

linkedin_ui_api_automation/
│
├── init.py # Marks the folder as a package
├── browser_wrapper.py # WebDriver initialization
├── conftest.py # PyTest setup and fixtures
├── linkedin_page.py # Page Object Model for LinkedIn UI
├── test_linkedin.py # LinkedIn login UI test
├── test_api.py # REST API test
├── pytest.ini # PyTest configuration
├── requirements.txt # Dependency list
├── report.html # Generated test report
├── README.md # Project documentation


### 1. Clone the Repository

git clone https://github.com/saigayathri04/linkedin-ui-api-automation.git
cd linkedin-ui-api-automation

2. (Optional) Create and Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows

4. Install Dependencies
pip install -r requirements.txt

▶️ Running the Tests
To execute the test suite and generate an HTML report:
pytest --html=report.html --self-contained-html
After the run, open report.html in your browser to view the results.

Test Summary:
=============

test_linkedin.py	Tests valid and invalid login scenarios
test_api.py	Validates API response and payload
linkedin_page.py	Contains web element locators and actions
browser_wrapper.py	Handles WebDriver setup and teardown

Screenshots:
============
Screenshots are captured for both passing and failing scenarios to help with validation and debugging.

HTML Reports:
=============
Each test run generates a report.html file containing:

Test case results (pass/fail)
Execution time
Environment details
Screenshots (if enabled)

The report supports sorting and filtering for easy navigation and debugging.

Planned Enhancements:
=====================
Retry failed tests using pytest-rerunfailures
CI integration with Jenkins
Secure credential handling using .env files
Enable parallel test execution with pytest-xdist

Maintainer:
============
Sai Gayathri
GitHub: @saigayathri04
