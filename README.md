# LinkedIn Login Automation Suite – UI + API Testing

This project combines Selenium-based UI automation and API validation using Python's `requests` module. Tests are organized using PyTest, focusing on LinkedIn login functionality through both frontend and backend layers. HTML reports are generated using `pytest-html`.


## ⚙️ Tech Stack Overview

| Tool           | Purpose                                |
|----------------|----------------------------------------|
| Python         | Language used for scripting            |
| Selenium       | Automates LinkedIn login via web UI    |
| PyTest         | Framework for organizing and running tests |
| Requests       | Sends and validates REST API calls     |
| pytest-html    | Generates HTML reports after test run  |
| Git & GitHub   | Version control and hosting            |
| PyCharm        | Development environment                |

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


## 🔧 Getting Started

### 1. Clone the Repository

git clone https://github.com/saigayathri04/linkedin-ui-api-automation.git
cd linkedin-ui-api-automation
2. (Optional) Create and Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
3. Install Dependencies
pip install -r requirements.txt
▶️ Running the Tests
To execute the full test suite and generate an HTML report:

pytest --html=report.html --self-contained-html
Open report.html in your browser to view the results.

🧪 Test Summary
File	Description
test_linkedin.py	Tests valid/invalid login scenarios
test_api.py	Validates API response & payload
linkedin_page.py	Holds element locators and actions
browser_wrapper.py	WebDriver setup logic

📸 Screenshots on Pass and Failure.
It capture both positive and negative scenarios

📄 HTML Reports
Each test run generates a report.html file containing:

Test results (pass/fail)

Execution time

Environment info

Screenshots

🚀 Planned Enhancements
Retry failed tests using pytest-rerunfailures

Integrate with Jenkins for CI/CD

Dockerize the test suite

Use .env files for credential management

Enable parallel test execution using pytest-xdist

👩‍💻 Maintainer
Sai Gayathri
GitHub: @saigayathri04

