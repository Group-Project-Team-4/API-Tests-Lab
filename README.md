# API Tests Lab
This lab exists as a [Git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) for [this web app repository](https://github.com/Group-Project-Team-4/Web-App) because the test scripts in this lab require the web application to be running. Instead of cloning this repository directly, you can just clone the web app repository and navigate to the `tests/rest_api` directory. The below documentation serves to outline the API functions that will be tested, as well as the process for testing API's.

## 1. Introduction
This lab repository contains scripts and documentation for testing a web application's REST API. It contains scripts for testing the API with the built-in Python `requests` library, as well as instructions for testing with the Postman GUI application.

**WARNING**: The scripts included in this repository are **NOT** Pytest scripts. This lab is about testing an API as a whole from outside of the program code, hence the use of the `requests` library and the Postman application to send requests to the running application externally. Follow the directions below to run the scripts properly.

## 2. Running the test scripts

**IMPORTANT NOTES:**
- The tests depend on the Python `requests` library which is installed in the virtual environment. You will need to activate the virtual environment before running both the tests and the application.
- The web app needs to be actively running when the test scripts are executed. You will most likely need to open another terminal window to run both at once. Make sure you activate the virtual environment in both terminals.
- The database for the application uses a unique primary key for the item ID's and it uses a counter to generate new ID's. However, when testing the POST method of the API, it will increment the ID counter without adding a new entry to the database (as it deletes the test entry once finished to clean up after the test). This will create gaps between ID values. For this reason, it might be important to run the `flask --app clothing_store init-db` command once concluded with testing to make sure the database is reset back to default.


### Instructions

1. Follow the instructions listed [here](https://github.com/Group-Project-Team-4/Web-App/blob/main/README.md) to create a virtual environment, install the dependencies, and run it. 

2. You can then run any individual tests you want with the command `python <file name>.py`. If you want to run all of them at once, run the `test_all.py` file with `python test_all.py`.

### How do they work?
Feel free to open the files in your text editor to check the code used to test the API. They all feature comments that explain and describe each step of the process and what is being tested at each point.

## 3. Testing Philosophy

### What is being tested?

The web application supports the following 5 API calls that need to be tested:
- `GET` at `/api/products` to retrieve a list of all products currently in the database.
- `GET` at `/api/products/<id>` to retrieve the information about a specific product in the database with the specified ID.
- `POST` at `/api/products` to add a new product to the database.
- `PUT` at `/api/products/<id>` to change the values of the product with the specified ID.
- `DELETE` at `/api/products/<id>` to remove a product with a specified ID from the database.

### Testing Strategy
For this lab, there are both provided Python scripts to test the API, as well as instructions for testing the API manually using the Postman application. The testing strategy of the scripts is to make a request, supply necessary data if necessary, and then test the response against multiple conditions. In the case of testing things like POST or PUT requests, the API's response to the request contains the data as it appears in the database (if the request was successful), so there is no need to follow up those requests with GET requests to make sure the changes "went through" successfully.