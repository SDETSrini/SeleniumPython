import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome"
    )



@pytest.fixture()
def setup(request):
    browser = request.config.getoption("browser_name")
    if browser == "Chrome":
        driver = webdriver.Chrome(executable_path="C:\\SriniData\\Softwares\\drivers\\chromedriver.exe")

    elif browser == "Firefox":
        driver = webdriver.Chrome(executable_path="C:\\SriniData\\Softwares\\drivers\\chromedriver.exe")
        # driver = webdriver.Firefox(executable_path="C:\\SriniData\\Softwares\\drivers\\geckodriver.exe")
        print("code for Firefox invoacation")

    driver.maximize_window()
    driver.get("https://www.amazon.in")
    request.cls.driver = driver
    yield
    driver.close()