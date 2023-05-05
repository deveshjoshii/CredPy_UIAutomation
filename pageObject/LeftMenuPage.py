import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LeftMenuPage:

    def __init__(self,driver):
        """contructor to initialize the LeftMenuPage objects
        :param driver:
        """
        self.driver=driver

    menu = (By.ID,"menu")


    def userClicksOnleftMenu(self):
        return self.driver.find_element(*LeftMenuPage.menu)




