# LinkedIn Login Automation – UI and API Testing

This project automates LinkedIn's login functionality using Selenium and validates a sample public API using the `requests` library. The tests are managed using the PyTest framework, and results are captured in an HTML report.

---

## Tools & Technologies

- **Python** – Scripting language
- **Selenium WebDriver** – Browser automation for UI testing
- **Requests** – Python HTTP library for API testing
- **PyTest** – Test runner and framework
- **pytest-html** – Plugin to generate HTML reports
- **Git & GitHub** – Version control and code hosting
- **PyCharm** – Development environment

---

## Project Structure

linkedin_ui_api_automation/
│
├── init.py # Makes the folder a Python package
├── browser_wrapper.py # Sets up and manages the WebDriver
├── conftest.py # Shared PyTest fixture configuration
├── linkedin_page.py # Page Object for LinkedIn login elements
├── test_linkedin.py # Test case for LinkedIn UI login
├── test_api.py # REST API validation test
├── pytest.ini # PyTest configuration file
├── requirements.txt # Lists required Python packages
├── report.html # Test report generated after execution
├── README.md # Project documentation

yaml
## How to Run

### 1. Clone the repository
'''bash
git clone https://github.com/saigayathri04/linkedin-ui-api-automation.git
cd linkedin-ui-api-automation
2. (Optional) Set up a virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the test suite and generate report
bash
Copy
Edit
pytest --html=report.html --self-contained-html
The report.html file will be created in the root directory. You can open it in a browser to view the test results.

Test Overview
File	Description
test_linkedin.py	Tests login with valid and invalid data
test_api.py	Validates API response status and payload
linkedin_page.py	Contains web element locators and actions
browser_wrapper.py	Manages browser startup and teardown

Optional: Screenshots on Failure
You can enhance the tests by saving screenshots when a test fails. These can be added using try-except blocks or PyTest hooks and stored in a dedicated folder.

Future Improvements
Add retries for flaky tests

Integrate with CI tools like Jenkins

Use .env files to manage sensitive data

Enable parallel test execution with pytest-xdist

Containerize the setup using Docker

Maintainer
Sai Gayathri
GitHub: @saigayathri04
