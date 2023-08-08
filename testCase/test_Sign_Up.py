import json
import time

import pytest

from testData.fbSignUpData import SignUp
from utilities.base import Base
from pageObject.SignUpPage import Test_SignUpPage


class Test_Sign_Up(Base):


    def test_signUP(self,getData):

        driver=self.driver
        # executor_object = {
        #     'action': 'setSessionName',
        #     'arguments': {
        #         'name': 'Test_Sign_UP'
        #     }
        # }
        # browserstack_executor = 'browserstack_executor: {}'.format(json.dumps(executor_object))
        # driver.execute_script(browserstack_executor)
        SignUpPage=Test_SignUpPage(driver)
        # driver.implicitly_wait(15)
        Base.cookie_consent(self.driver)
        SignUpPage.user_clicks_SingUP()
        SignUpPage.user_clicks_Create_account()#Activate account

        SignUpPage.user_clicks_fbSSO_option()
        SignUpPage.user_input_email_id(getData["email"])
        SignUpPage.user_input_password(getData["pas"])
        SignUpPage.user_clicks_next_button()
        SignUpPage.user_lands_on_onboarding_screen()
        # SignUpPage.user_verify_bullets_on_step0()
        SignUpPage.user_clicks_on_next_step0()
        SignUpPage.user_verify_step1()
        SignUpPage.user_selects_credit_score_option()
        SignUpPage.user_verify_step2()
        SignUpPage.user_verify_step2_list()
        SignUpPage.user_verify_screen3()
        SignUpPage.user_click_on_get_my_credit()
        Base.cookie_consent(self.driver)
        SignUpPage.user_verify_enrol_landing_page()
        SignUpPage.user_navigate_to_profile()
        # Base.cookie_consent(self.driver)
        SignUpPage.user_delete_the_account()
        # driver.navigate()

    @pytest.fixture(params=SignUp.user1)
    def getData(self, request):
        return request.param














