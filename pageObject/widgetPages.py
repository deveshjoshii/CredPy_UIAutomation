from datetime import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select





class Widget_Page_Object:

    def __init__(self,driver):
        self.driver=driver


    widget_loan_purpose=(By.ID,"loan_purpose")
    widget_loan_amount=(By.XPATH,"//input[@name='loan_amount']")
    widget_credit_score=(By.ID,"credit_score")
    widget_state_value=(By.ID,"state")
    widget_loan_page_title=(By.XPATH,"//h1[contains(@class,'entry-title')]")



    def user_validate_all_the_urls_and_validate_default_values(self,url):
        self.driver.get(url)

    def user_assert_loan_purpose(self,expected):
        purpose=self.driver.find_element(*Widget_Page_Object.widget_loan_purpose).get_attribute("value")
        print(purpose)
        assert expected==purpose


    def user_validate_loan_amount(self,expectedLoan):
        amount=self.driver.find_element(*Widget_Page_Object.widget_loan_amount).get_attribute("value")
        print(amount)
        print(expectedLoan)
        assert amount==expectedLoan



