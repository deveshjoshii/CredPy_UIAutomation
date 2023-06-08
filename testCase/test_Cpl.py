import time

import pytest

from pageObject.PersonalLoanPage import PersonalLoan
from testData.personalLoanData import CPLData
from utilities.base import Base
from selenium import webdriver


class Test_CPL(Base):

    def test_cpl(self,getData):
        driver=self.driver
        driver.implicitly_wait(15)
        cpl_page_obj=PersonalLoan(self.driver)
        Base.cookie_consent(self.driver)

        cpl_page_obj.user_clicks_on_cpl_homepage()
        # time.sleep(4)

        cpl_page_obj.user_click_on_next_button()
        cpl_page_obj.user_assert_error_message()
        cpl_page_obj.user_click_on_did_not_find_option()
        cpl_page_obj.user_assert_on_loan_purpose_drop_down()
        cpl_page_obj.user_fetch_loan_purpose()
        cpl_page_obj.user_selects_loan_purpose(getData["purpose"])
        cpl_page_obj.user_click_on_next_button()
        # time.sleep(10)

        cpl_page_obj.user_assert_progress_bar(getData["p1"])
        cpl_page_obj.user_clicks_on_next_on_loan_amount_page()
        cpl_page_obj.user_assert_error_on_loan_details_page()
        cpl_page_obj.user_enter_loan_amount(getData["loanAmount"])


        # try:
        cpl_page_obj.user_open_term_drop_down()
        cpl_page_obj.user_selects_loan_term(getData["loanTerm"])
        # driver.refresh()
        # time.sleep(5)


        cpl_page_obj.user_clicks_on_next_on_loan_amount_page()



        cpl_page_obj.user_assert_progress_bar(getData["p2"])
        cpl_page_obj.user_click_on_next()
        cpl_page_obj.user_assert_error_on_state()
        cpl_page_obj.user_enters_state(getData["state"])
        cpl_page_obj.user_click_on_next()
        # time.sleep(3)


        cpl_page_obj.user_assert_progress_bar(getData["p3"])
        cpl_page_obj.user_click_on_next_on_credit_score()
        cpl_page_obj.user_assert_error_on_credit_page()
        # time.sleep(2)

        cpl_page_obj.user_fetch_all_the_credit_score(['Excellent (720+)','Good (660-719)','Fair (620-659)','Poor (<619)'])
        cpl_page_obj.user_select_credit_prefrence(getData["credit_score"])
        cpl_page_obj.user_click_on_next_on_credit_score()
        # time.sleep(2)


        cpl_page_obj.user_assert_progress_bar(getData["p4"])
        cpl_page_obj.user_click_on_income_next_button()
        # cpl_page_obj.user_click_on_tool_tip()


        # time.sleep(10)
        # cpl_page_obj.user_assert_tool_tip_pop_up()
        # cpl_page_obj.user_close_tool_tip()
        # time.sleep(2)
        cpl_page_obj.user_assert_monthly_income_message()
        cpl_page_obj.user_enter_monthly_amout(getData["month_amount"])

        cpl_page_obj.user_click_on_income_next_button()
        # time.sleep(3)

        cpl_page_obj.user_open_advertiser_disclosure()
        cpl_page_obj.user_assert_link_in_the_advertiser_content()
        cpl_page_obj.user_close_advertiser_disclosure_pop_up()
        # time.sleep(3)
        cpl_page_obj.user_assert_loan_purpose(getData["purpose"])
        cpl_page_obj.user_assert_loan_amount(getData["loanAmount"])
        cpl_page_obj.user_assert_loan_term(getData["loanTerm"])
        cpl_page_obj.user_assert_credit_score(getData["credit_score"])
        cpl_page_obj.user_assert_lender_list(getData["lender_list"],getData["lender_count"])







    @pytest.fixture(params=CPLData.cpldata)
    def getData(self,request):
        return request.param


