# Framework_Selenium_Behave_POM_Allure
----------------------------------------
Let's to automate test cases of webapps using this framework written with Python. It is necessary to install the next elements: 

1.	Download Selenium Webdriver for the respect version of Google Chrome
2.	Download Python 3.8 
3.	Download Allure
4.	Install the next packages by console
4.1	pip install behave
4.2	pip install allure-behave 
4.3	pip install selenium 

To execute test cases, use this command: 
- behave -f allure_behave.formatter:AllureFormatter -o allure-report ./features

To see allure-report, use this command: 
- Allure serve allure-report
