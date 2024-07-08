# Swagger Petstore API Testing Framework

Automated API tests are written for the [Petstore server](https://petstore.swagger.io/).

## Getting Started

To use and run tests, follow these steps:

1. Clone the to your local machine using the following command:
```
git clone https://github.com/YuryHerasimau/petstore-swagger-api-testing.git
```
2. Navigate to the cloned repository directory on your local machine.
3. Install the required dependencies by running the following command:
```
pip install -r requirements.txt
```
4. Activate the virtual environment by running the appropriate command based on your operating system. For Windows, you can use:
```
source env/Scripts/activate
```
5. Сreate a `.env` file in the root directory based on the `.env.template`
6. Finally, run the tests using pytest with the following command:
```
pytest --alluredir=allure_result
```
7. After running the tests, serve the Allure report using the following command:
```
allure serve allure_result
```