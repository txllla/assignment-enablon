# assignment_enablon

This project presents a set of autotests for the TodoMVC application. 

### 10 test cases in total

#### 6 basic positive scenarios (Minimal Acceptance Testing coverage):
1. Add new todo
2. Edit todo
3. Delete todo
4. Mark todo as completed
5. Check todos counter after adding new todo
6. Clear completed todo

#### 4 negative scenarios (Acceptance Testing coverage):
1. Add 2 todos with the same name
2. Edit todo when there are 2 todos with the same title
3. Delete todo when there are 2 todos with the same title
4. Change todo title to empty string

### Technologies

The following technology stack was used to write autotests: python, pytest, selenium; allure used for reporting

### Patterns used:
1. To reduce code duplication and convenient use of page elements, the PageObject pattern was used
2. In tests, frequently repeated pieces of code were presented as reusable steps in the steps folder
3. Frequently used utilities have also been moved into separate functions (they can be found in the utils folder)
4. Reusable classes were written to represent page elements (they can be found in the elements folder)
5. To prevent the possibility of creating several webdriver instances in the test, the Singleton pattern was used

### How the tests are organized

All tests are stored in the file **test_todo_page.py**

To run the tests, 4 configuration files are required:
1. test_data.yaml - it is stored in the tests folder, it contains test data
2. browser_config.yaml - it is stored in the root of the project, it contains browser settings
3. logger_config.yaml - it is stored in the root of the project, it contains the logger settings
4. webdriver_config.yaml - it is stored in the root of the project, it contains the webdriver settings

>To run tests with allure results -> run from **tests** folder:
```pytest --alluredir=../tmp/allure-results test_todo_page.py```

>To generate report from allure results after running the tests -> run from **tests** folder:
```allure serve ../tmp/allure-results```
