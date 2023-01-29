# README
This code is a collection of tests that test the functionality of a patient identifier endpoint.

## Technologies Used
- Python 3
- requests: Used to make HTTP requests to the endpoint
- json: Used to parse the JSON response
- jsonpath: Used to extract specific values from the JSON response
- pytest: Used as the test framework
- Selenium: Webdriver to run automated tests
- Chrome browser

## How to Run the Tests
1. 
2. Ensure that you have the necessary dependencies installed (see the requirements.txt)
3. Run the following command to launch the test server 
```cmd 
cd api-server 
flask run
```
4. Run the follwing command 
```cmd
cd ..
pytest
``` 
in the directory where the test file is located.