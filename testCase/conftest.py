import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    """this function define config options and helps parameterize them
    :param parser:
    :return: NONE
    """
    parser.addoption(
        "--browser_name",action="store",default="chrome"
    )




#


@pytest.fixture()
def setup(request):
    """tear down scripts,this function also selects browser on the basis of user input
    i.e. chrome or firefox
    :param request:
    :return: returns driver object    """

    browser_name = request.config.getoption("browser_name")
    if browser_name=="chrome":
        optionC = webdriver.ChromeOptions()
        # service_obj = Service("assets\\chromedriver.exe")
        optionC.binary_location=r'C:/Program Files/Google/Chrome/Application/chrome.exe'
        # driver = webdriver.Chrome(service=service_obj,options=optionC)
        driver = webdriver.Chrome('assets\\chromedriver.exe')
        driver.get("https://www.credello.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

        request.cls.driver = driver
    elif browser_name=="fire_fox":
        optionF = webdriver.FirefoxOptions()
        service_obj2 = Service("assets\\geckodriver.exe")
        optionF.binary_location = r'C:/Users/devesh.joshi/AppData/Local/Mozilla Firefox/firefox.exe'
        driver = webdriver.Firefox(service=service_obj2, options=optionF)
        driver.get("https://uat.credello.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)
        request.cls.driver = driver
    yield
    # driver.close()
    driver.quit()


