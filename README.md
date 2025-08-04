# 🤖 LinkedIn Login Automation Suite – UI + API Testing

This project combines **Selenium-based UI automation** and **API validation** using Python's `requests` module, structured using **PyTest**. It focuses on testing LinkedIn login functionality through both front-end and back-end layers. Clean reporting is integrated via `pytest-html` to visualize the results.

---

## ⚙️ Tech Stack Overview

| Tool           | Role in Project                     |
|----------------|--------------------------------------|
| Python         | Scripting language for automation    |
| Selenium       | Automates LinkedIn web UI actions    |
| PyTest         | Organizes and runs test cases        |
| Requests       | Used for REST API validation         |
| pytest-html    | Generates visual HTML reports        |
| Git + GitHub   | Version control and repo hosting     |
| PyCharm        | Development environment              |

---

## 🧱 Folder Structure

linkedin_ui_api_automation/
│
├── init.py # Makes this a Python package
├── browser_wrapper.py # Initializes the WebDriver
├── conftest.py # Shared PyTest setup/configuration
├── linkedin_page.py # Page Object Model for LinkedIn UI
├── test_linkedin.py # UI login test case
├── test_api.py # REST API test validations
├── pytest.ini # PyTest configuration file
├── requirements.txt # All dependencies listed here
├── report.html # Generated after each test run
├── README.md # Project documentation (this file)

yaml
Copy
Edit

---

## 🔧 Getting Started

### 1. Clone the Repository

''bash
git clone https://github.com/saigayathri04/linkedin-ui-api-automation.git
cd linkedin-ui-api-automation
2. (Optional) Create and Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
3. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
✅ Running the Tests
To execute the complete test suite and generate an HTML report:

bash
Copy
Edit
pytest --html=report.html --self-contained-html
You can open report.html in any browser to view the results.

🔍 Test Case Summary
File	Description
test_linkedin.py	Automates login test via web UI
test_api.py	Verifies API status code and payload
linkedin_page.py	Encapsulates LinkedIn page elements
browser_wrapper.py	WebDriver init logic

🖼️ Screenshots on Failure (Optional)
You can enhance test feedback by capturing screenshots on test failure and saving them under an assets/ directory using PyTest hooks or exception handling.

📄 HTML Reports
After each run, a detailed HTML report (report.html) is auto-generated with:

Test results

Execution time

Environment details

(Optional) Screenshots

🛠 Planned Enhancements
 Add retry mechanism for unstable tests using pytest-rerunfailures

 Integrate with Jenkins for scheduled runs and CI/CD

 Add Docker support for containerized test runs

 Secure credential management using .env files

 Enable parallel execution using pytest-xdist

👩‍💻 Maintainer
Sai Gayathri

GitHub: @saigayathri04
