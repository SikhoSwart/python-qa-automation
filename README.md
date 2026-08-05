# Python QA Automation Framework

A robust, scalable test automation framework built with Python, demonstrating both API and UI testing capabilities. This project utilizes industry-standard tools and design patterns to ensure maintainable and reliable automated checks.

## Tech Stack & Architecture

*   **Language:** Python 3.11+
*   **Test Runner:** `pytest`
*   **API Testing:** `requests` (Testing CRUD operations on [Restful-Booker](https://restful-booker.herokuapp.com/))
*   **UI Automation:** `Playwright` (Testing the [SauceDemo](https://www.saucedemo.com/) web application)
*   **CI/CD:** GitHub Actions
*   **Design Patterns:** Page Object Model (POM), Pytest Fixtures, API Client Wrappers

## Project Structure

```text
├── .github/workflows/   # CI/CD pipeline configuration
├── api_clients/         # HTTP client wrappers for API interactions
├── page_objects/        # UI Page Object Model classes
├── tests/
│   ├── api/             # API test scripts
│   ├── ui/              # UI end-to-end test scripts
│   └── conftest.py      # Shared pytest fixtures (auth, setup/teardown)
├── pytest.ini           # Pytest configuration
└── requirements.txt     # Project dependencies
