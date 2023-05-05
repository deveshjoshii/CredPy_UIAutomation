import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.base import Base


class Test_SignUpPage(Base):

    def __init__(self,driver):
        self.driver=driver


    sign_up = (By.XPATH, "//div//button[text()='Sign Up']")
    fb_SSO = (By.XPATH, "//div[contains(@class,'SocialSignIn')]//p[contains(text(),'Facebook')]")
    email_input_box = (By.NAME, "email")
    pass_input_box = (By.NAME, "pass")
    next_button_on_emailPage = (By.ID, "loginbutton")
    cookie_pop_up = (By.XPATH, "//button[contains(@class,'Button')]//h3[text()='Got it']")
    onboarding_step0=(By.ID,"step0")



    def user_close_consent_popUp(self):
        return self.driver.find_element(*Test_SignUpPage.cookie_pop_up)

    def user_clicks_SingUP(self):
        print(self.driver.find_element(*Test_SignUpPage.sign_up))
        return self.driver.find_element(*Test_SignUpPage.sign_up)

    def user_clicks_fbSSO_option(self):
        return self.driver.find_element(*Test_SignUpPage.fb_SSO)


    def user_input_email_id(self):
        return self.driver.find_element(*Test_SignUpPage.email_input_box)

    def user_input_password(self):
        return self.driver.find_element(*Test_SignUpPage.pass_input_box)

    def user_clicks_next_button(self):
        return self.driver.find_element(*Test_SignUpPage.next_button_on_emailPage)

    def user_check_additional_screenSSO(self):
        return self.driver.find_element(*Test_SignUpPage.additional_pop_up_SSO_screen)

    def user_lands_on_onboarding_screen(self):
        WebDriverWait(self.driver,20,ignored_exceptions=["ElementNotVisible","ElementNotClickable"]).until(expected_conditions.visibility_of_element_located((Test_SignUpPage.onboarding_step0)))
        return self.driver.find_element(*Test_SignUpPage.onboarding_step0).is_Displayed()




