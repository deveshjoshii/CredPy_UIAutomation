import json
import time

import pytest
from pageObject.DebtConsolidationPage import DcprPage
from utilities.base import Base


class Test_DCPR(Base):
    
    def test_dcpr_flow(self):
        driver=self.driver
        executor_object = {
            'action': 'setSessionName',
            'arguments': {
                'name': 'Test_DCPR'
            }
        }
        browserstack_executor = 'browserstack_executor: {}'.format(json.dumps(executor_object))
        driver.execute_script(browserstack_executor)
        
        # removed self.driver
        Base.cookie_consent(driver)
        dcpr=DcprPage(driver)
        dcpr.user_click_on_dcpr_link_on_hp()
        dcpr.user_verify_account_tiles_on_the_page()
        dcpr.user_clicks_on_next_button()
        dcpr.user_verify_error_on_the_page()
        time.sleep(7)
        dcpr.user_select_debt_type()
        dcpr.user_click_on_next()   
        dcpr.user_clicks_on_have_more_account()     
        time.sleep(5)
        dcpr.user_verify_progress_bar('12%')
        dcpr.user_verify_credit_score_label()
        dcpr.user_click_on_next_on_credit_score_page()

        dcpr.user_verify_progress_bar_on_prefrece_page('23%')
        dcpr.user_selects_pref_labels()
        dcpr.user_click_on_next_on_prefrence_page()

        dcpr.user_verify_progress_bar_on_home_owner_page('34%')
        dcpr.user_selects_home_owner_as_yes()
        dcpr.user_clicks_on_next_on_home_owner_page()

        dcpr.user_clicks_on_enter_debt()

        # debt details 
       
        data1=[2400,22.22,456]
        data2=[2400,22.22,456]

        totaldebtamount=data1[0]+data2[0]
        resDebt=(format (totaldebtamount, ',d'))
        Combapr=f"{(data1[1]+data2[1])/2:.2f}"
        print(Combapr)
        totalMonth=data1[2]+data2[2]
        print(totalMonth)

        
        # dcpr.user_verify_progress_on_debt_details_page('45%')
        dcpr.user_verify_no_of_account_on_the_page(2)
        dcpr.user_enters_first_cards_details(data1[0],data1[1],data1[2])
        dcpr.user_enters_second_cards_details(data2[0],data2[1],data2[2])

        dcpr.user_click_on_next_debt_details_page()
        dcpr.user_verify_total_debt(resDebt)
        dcpr.user_verify_comb_apr(Combapr)
        dcpr.user_verify_comb_emi(totalMonth)
        dcpr.user_clicks_on_next_debt_summary_page()

        #  month income
        dcpr.user_verify_month_income_field_name()
        dcpr.user_clicks_on_too_tip()
        dcpr.user_enters_month_amount_dcpr(2300)
        dcpr.user_selects_yes_for_month_payment()
        dcpr.user_clicks_on_next_month_income()

        # locationpage

        # dcpr.user_accespts_location_alert()
        dcpr.user_enter_zip_code()
        time.sleep(4)
        dcpr.user_continue_with_zip_code_value()
        dcpr.user_clicks_on_next_on_location_page()

        # mortgage page
        dcpr.user_enters_mortgage_amount()
        dcpr.user_enters_mortgage_apr()
        dcpr.user_selects_mortgage_year()
        dcpr.user_selects_mortgage_year_from_drop_down()
        dcpr.user_selects_term_from_the_drop_down()
        dcpr.user_clicks_on_next_on_mortgage_page()

        #  reco page
        dcpr.user_verify_lender_listing_on_reco()
        




        






    
        
        

    



    

    