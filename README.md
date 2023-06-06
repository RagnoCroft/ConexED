# Cranium Cafe Regression Test Suite
This repository contains a set of regression tests for the Cranium Cafe web application using Selenium WebDriver.

## Prerequisites
Before running the regression tests, ensure that you have the following prerequisites set up:

Python 3.x installed on your system.
Selenium Python package installed. You can install it using pip:
```python
pip install selenium
```
Chrome browser installed on your system.
ChromeDriver executable downloaded and placed in the appropriate location. You can download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure to download the version compatible with your Chrome browser version.

## Running the Tests
To run the regression tests, follow the steps below:

Clone this repository to your local machine.
Navigate to the repository directory:
```bash
cd ConexED
```
Open the Python script **ConexED_Assessment_Login.py** and modify the **chrome_driver_path** variable with the path to your ChromeDriver executable.
Open a terminal or command prompt and execute the following command to run the tests:
```python
python ConexED_Assessment_Login.py
```
The regression tests will execute and provide the output indicating whether each test passed or failed.

## Test Cases
The regression tests cover the following test cases:

Navigates to Cranium Cafe Website

Verifies that the user can navigate to the Cranium Cafe website.
Search and Select Cranium Cafe - Test

Verifies that the user can search for and select the 'Cranium Cafe - Test' option.
Guest Registration

Verifies that the user can complete the guest registration process.
Login with Registered Credentials

Verifies that the user can log in using the registered credentials.
Please refer to the **ConexED_Assessment_Login.py** file for the detailed implementation of each test case.

## Notes
The commented code for the Gmail login scenario is left as a hypothetical scenario due to complications with Selenium WebDriver and Google's security policies. The corresponding regression tests for Gmail login are not implemented.
This repository is intended for regression testing purposes and does not cover all possible test scenarios. It serves as a starting point for building a more comprehensive test suite.
Feel free to explore, enhance, and customize the regression tests according to your specific requirements.

**Disclaimer:** The tests in this repository were created based on the provided code snippet, and they assume that the Cranium Cafe web application is functioning as expected. If there are any changes or updates to the application, the tests may need to be modified accordingly.

For any issues or questions, please open an issue in this repository.

Happy testing!
