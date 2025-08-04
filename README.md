# 🔗 LinkedIn UI + API Automation Suite

A hybrid automation framework using **Selenium WebDriver** and **REST API testing** with 'requests` library, orchestrated through **PyTest**. This project validates LinkedIn login functionality (UI) and REST API responses, with rich HTML reporting — making it ideal for portfolio demonstrations and interviews.

---

## 🛠 Technologies Used

| Tool            | Purpose                        |
|-----------------|---------------------------------|
| Python          | Core programming language       |
| Selenium        | Web UI automation               |
| PyTest          | Test execution framework        |
| Requests        | REST API testing                |
| pytest-html     | HTML test reporting             |
| Git + GitHub    | Version control & repo hosting  |
| PyCharm         | IDE used for development        |

---

## 📦 Project Structure

linkedin_ui_api_automation/
│
├── init.py # Marks directory as a package
├── browser_wrapper.py # Sets up Selenium WebDriver
├── conftest.py # PyTest fixtures for setup/teardown
├── linkedin_page.py # Page Object Model (POM) for LinkedIn login
├── test_linkedin.py # UI test for LinkedIn login
├── test_api.py # REST API validation test
├── pytest.ini # PyTest configuration
├── requirements.txt # List of dependencies
├── report.html # Auto-generated test report
├── README.md # Project documentation

yaml
Copy
Edit
## 🚀 Setup Instructions

### 1. Clone the Repository

'''bash
git clone https://github.com/saigayathri04/linkedin-ui-api-automation.git
cd linkedin-ui-api-automation
2. (Optional) Create & Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate    # On Windows
3. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
▶️ Run Tests
Run all tests and generate a report:

bash
Copy
Edit
pytest --html=report.html --self-contained-html
After execution, open report.html in your browser to view the detailed test report.

🔍 Test Breakdown
File	Description
test_linkedin.py	Validates LinkedIn login via UI
test_api.py	Verifies API response data and status
linkedin_page.py	Encapsulates UI locators and actions
browser_wrapper.py	WebDriver setup and teardown logic

📸 Screenshots (Optional)
You can enhance this by saving failure screenshots under an assets/ directory using PyTest hooks or try-except blocks in your test files.

📑 HTML Reporting
An HTML report (report.html) is auto-generated using pytest-html, showing:

Test case results

Duration

Environment info

Optional screenshots

📈 Future Enhancements
 Retry logic for flaky tests using pytest-rerunfailures

 Integrate with Jenkins for CI/CD automation

 Add a Dockerfile for containerized test execution

 Use .env files to securely manage credentials

 Enable parallel execution with pytest-xdist

👩‍💻 Author
Sai Gayathri

GitHub: @saigayathri04

⭐ Star this repo if you found it helpful or used it in your portfolio!
