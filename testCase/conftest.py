import json

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.firefox.options import Options

driver = None
#  varibales to store exception info
test = None
status_tag = None
line = None
duration = None
exception = None

def pytest_addoption(parser):
    """this function define config options and helps parameterize them
    :param parser:
    :return: NONE
    """
    parser.addoption(
        "--browser_name",action="store",default="chrome"

    )
    parser.addoption(
    "--end_point", action = "store", default = "https://www.credello.com/"
    )

#  setup starts here
@pytest.fixture()
def setup(request):
    """tear down scripts,this function also selects browser on the basis of user input
    i.e. chrome or firefox
    :param request:
    :return: returns driver object    """
    global driver
    global session

    browser_name = request.config.getoption("browser_name")
    endpoint=request.config.getoption("end_point")
    if browser_name=="chrome":
        
        # service = ChromeService(executable_path=ChromeDriverManager().install())
        # --chrome_options = webdriver.ChromeOptions()
        # --chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--headless')
        # --chrome_options.add_argument('--disable-dev-shm-usage')
        # --chrome_options.add_argument("--disable-setuid-sandbox")
        driver=webdriver.Chrome()
        # service=service,options=chrome_options
        
        if endpoint=="prod":
            driver.get("https://www.credello.com/")
            driver.maximize_window()
            driver.implicitly_wait(15)
        elif endpoint=="dev":
            driver.get("https://dev2.credello.com/")
            driver.maximize_window()
            driver.implicitly_wait(15)
        elif endpoint=="qa":
            driver.get("https://qa.credello.com/")
            driver.maximize_window()
            driver.implicitly_wait(15)
        elif endpoint=="uat":
            driver.get("https://uat.credello.com/")
            driver.maximize_window()
            driver.implicitly_wait(15)
        else:
            driver.get("https://www.credello.com/")
            driver.maximize_window()
            driver.implicitly_wait(15)
        request.cls.driver = driver
        session=driver.session_id
        print(session)
        

    elif browser_name=="fire_fox":
        optionF = webdriver.FirefoxOptions()
        service_obj2 = Service("assets\\geckodriver.exe")
        optionF.binary_location = r'C:/Users/devesh.joshi/AppData/Local/Mozilla Firefox/firefox.exe'
        driver = webdriver.Firefox(service=service_obj2, options=optionF)
        if endpoint=="prod":
            driver.get("https://www.credello.com/")
            driver.maximize_window()
            driver.implicitly_wait(15)
        elif endpoint=="dev":
            driver.get("https://dev2.credello.com/")
            driver.maximize_window()
            driver.implicitly_wait(15)
        elif endpoint=="qa":
            driver.get("https://qa.credello.com/")
            driver.maximize_window()
            driver.implicitly_wait(15)
        elif endpoint=="uat":
            driver.get("https://uat.credello.com/")
            driver.maximize_window()
            driver.implicitly_wait(15)
        else:
            driver.get("https://www.credello.com/")
            driver.maximize_window()
            driver.implicitly_wait(15)
        request.cls.driver = driver


    yield
    # driver.close()
    driver.quit()

# Embed screen shots in html report

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

# capture screenshots
def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)


# track the test execution, stores all the exceptions
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    global test, status_tag, line, duration, exception
    outcome = yield
    test_result = outcome.get_result()
    if test_result.when == "call":
       (filename,line,name)= item.location
       test=item.nodeid
       status_tag=test_result.outcome
       line = line
       duration = call.duration
       exception = call.excinfo
    #    print(test_result.outcome)
    #    print("This is result", test_result.outcome)
    #    print(f"test {test}")
    #    print(f"status {status_tag}")
    #    print(f"line {line}")
    #    print(f"duration {duration}")
    #    print(f"exception {exception}")
       exe=str(exception)

       if test_result.outcome=='failed':
            executor_object = {
                'action': 'setSessionStatus',
                'arguments': {
                    'status': "failed",
                    'reason': exe
                }
            }
            browserstack_executor = 'browserstack_executor: {}'.format(json.dumps(executor_object))
            driver.execute_script(browserstack_executor)
       else:
            executor_object = {
                'action': 'setSessionStatus',
                'arguments': {
                    'status': "passed",
                    'reason': exe
                }
            }
            browserstack_executor = 'browserstack_executor: {}'.format(json.dumps(executor_object))
            driver.execute_script(browserstack_executor)











