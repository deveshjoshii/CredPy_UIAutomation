from utilities.base import Base
from pageObject.SignUpPage import Test_SignUpPage


class Test_Sign_Up(Base):

    def test_signUP(self):

        sign_up_page=Test_SignUpPage(self.driver)
        sign_up_page.cookie_consent()
        sign_up_page.user_clicks_SingUP().click()
        sign_up_page.user_clicks_SingUP().click()#Activate account
        sign_up_page.user_clicks_fbSSO_option().click()
        sign_up_page.user_input_email_id().send_keys("9540720229")
        sign_up_page.user_input_password().send_keys("Devesh@1985")
        sign_up_page.user_clicks_next_button().click()
        sign_up_page.user_lands_on_onboarding_screen()














