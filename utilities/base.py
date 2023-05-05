import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class Base:

    cookie_pop_up = (By.XPATH, "//button[contains(@class,'Button')]//h1[text()='Got it']")


    def selectDropDown(self,locator,text):
        select=Select(locator)
        select.select_by_visible_text(text)

    def cookie_consent(self):

        try:
            if self.find_element(*Base.cookie_pop_up).is_displayed():
                self.find_element(*Base.cookie_pop_up).click()
        except:
            print("Element not visible.")

    def getLogger(self):
        logger=logging.getLogger(__name__)
        fh=logging.FileHandler("logfile.log")
        formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        handle=logger.addHandler(fh)
        logger.setLevel(logging.DEBUG)
        return logger




















