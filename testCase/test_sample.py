import os

from selenium import webdriver
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY")

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability("browserVersion", "103")
chrome_options.set_capability("platformName", "Windows 10")
URL = "https://{}:{}@hub.browserstack.com/wd/hub".format(BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY)
driver = webdriver.Remote(
    command_executor=URL,
    options=chrome_options
)

# driver = webdriver.Remote(command_executor=URL, options=options)
driver.get("http://www.google.com")
driver.quit()



