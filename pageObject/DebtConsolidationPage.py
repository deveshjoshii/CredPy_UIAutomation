import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
class DcprPage:

    # constructor initialization happens here
    
    def __init__(self,driver):
        self.driver=driver

    # element creations
    
    dcpr_link_on_homepage=(By.XPATH,"//div[@class='productIcons']//a[contains(@href,'best-debt-consolidation-methods')]")
    debt_tiles_on_dcprpage=(By.XPATH,"//div[contains(@class,'ManageDebtGrid')]//h3") 
    error_message_On_landin_page=(By.XPATH,"//div[contains(text(),'Please select at least one debt')]")   
    next_on_landing_page=(By.ID,"nextStep")
    have_more_account_popup=(By.XPATH,"//div[contains(@class,'MuiPaper-root')]")
    option_yes=(By.ID,"yes")
    # credit score page    
    credit_score_label=(By.XPATH,"//div[contains(@class,'CreditScorePref')]//button//h3")
    next_on_credit_score_page=(By.ID,"next")
    # user prefrence page
    user_prefrence_labels=(By.XPATH,"//div[contains(@class,'DebtConsolidationPref')]//h3")
    next_on_user_pref_page=(By.ID,"next")
    # home owner 
    home_owner_yes=(By.ID,"yes")
    next_on_home_owner_page=(By.ID,"next")
    # almost Done page
    enter_debt_details=(By.ID,"next")
    # debt details 
    numOfCards=(By.XPATH,"//div[contains(@id,'cardIndex')]")
    debt_card1=(By.ID,"cardIndex0")
    debt_card2=(By.ID,"cardIndex1")
    balance1=(By.ID,"balance1")
    balance2=(By.ID,"balance2")
    APR1=(By.ID,"interestRate1")
    APR2=(By.ID,"interestRate2")
    monthPay1=(By.ID,"minMonthlyPayment1")
    monthPay2=(By.ID,"minMonthlyPayment2")
    next_on_debt_details_page=(By.ID,"next")

    #  debt summary page
    total_debt=(By.ID,"totalDebt")
    com_apr=(By.ID,"combinedInterest")
    total_month_pay=(By.ID,"totalMonthlyPayment")
    next_on_debt_suammry_page=(By.ID,"next")

    #  monhtly income
    month_income_message=(By.XPATH,"//div[contains(@class,'income__Content')]//h3")
    income_tool_tip=(By.XPATH,"//div[contains(@class,'popupWrapper')]")
    income_text_box=(By.NAME,"monthlyIncome")
    next_on_debt_month_income_page=(By.ID,"next")
    will_you_be_able_to_pay_yes_option=(By.ID,"yes")

    #  location page
    zip_code_input=(By.ID,"zipCodeInput")
    continue_with_zip_code=(By.XPATH,"//div[contains(@class,'home-value')]//h3[contains(text(),'Continue')]")
    location_page_next=(By.ID,"next")
    no_home_value_error=(By.XPATH,"//div[contains(text(),'We could not find data for this zipcode.')]")

    #  mortage page 
    mortgage_amount=(By.NAME,"outstandingMortgage")
    mortgage_apr=(By.NAME,"mortgageInterest")
    mortgage_year=(By.ID,"combo-box-demo")
    mortgage_term=(By.ID,"select-mortgageTerm")
    year_drop_down=(By.ID,"//input[@aria-activedescendant='combo-box-demo-option-4']")
    term_in_drop_down=(By.XPATH,"//ul//li[contains(@data-value,'15')]")
    next_on_mortgage_page=(By.ID,"next")

    # reco page
    lender_listing=(By.ID,"lenderListing")

    # common objects
    progress_bar_on=(By.XPATH,"//div[contains(@class,'ProgressBar')]//span")

    # Action starts here
    
    def user_click_on_dcpr_link_on_hp(self):
        self.driver.find_element(*DcprPage.dcpr_link_on_homepage).click()

    def user_verify_account_tiles_on_the_page(self):
        debttypes=self.driver.find_elements(*DcprPage.debt_tiles_on_dcprpage)

    def user_clicks_on_next_button(self):
        self.driver.find_element(*DcprPage.next_on_landing_page).click()

    def user_verify_error_on_the_page(self):
        self.driver.find_element(*DcprPage.error_message_On_landin_page).is_displayed()

    def user_select_debt_type(self):
        dtypes=self.driver.find_elements(*DcprPage.debt_tiles_on_dcprpage)
        for i in dtypes:
            print(i.text)
            if i.text=='Credit cards':
                i.click()

    def user_click_on_next(self):
        self.driver.find_element(*DcprPage.next_on_landing_page).click()

    def user_clicks_on_have_more_account(self):
        yes=self.driver.find_element(*DcprPage.option_yes)
        print(f"this is yes object {yes}")
        yes.click()

    #  crditScorePage

    def user_verify_progress_bar(self,val):
        creditScoreProgress=self.driver.find_element(*DcprPage.progress_bar_on).text
        print(creditScoreProgress)
        assert creditScoreProgress==val

    def user_verify_credit_score_label(self):
        cs=self.driver.find_elements(*DcprPage.credit_score_label)
        assert len(cs)==4
        for i in cs:
            print(i.text)
            if i.text=='Excellent (720+)':
                i.click()

    def user_click_on_next_on_credit_score_page(self):
        self.driver.find_element(*DcprPage.next_on_credit_score_page).click()

    # user prefrence page

    def user_verify_progress_bar_on_prefrece_page(self,val):
        prgress=self.driver.find_element(*DcprPage.progress_bar_on).text
        assert prgress==val

    def user_selects_pref_labels(self):
        
        prefrences=self.driver.find_elements(*DcprPage.user_prefrence_labels)
        for i in prefrences:
            print(i.text)
            i.click()
        for i in prefrences:
            if i.text=='Reduce total interest':
               i.click()

    def user_click_on_next_on_prefrence_page(self):
        self.driver.find_element(*DcprPage.next_on_user_pref_page).click()         
        


    # HomeOwner Page

    def user_verify_progress_bar_on_home_owner_page(self,val):
        prgress=self.driver.find_element(*DcprPage.progress_bar_on).text
        try:
            assert prgress==val
        except Exception as e:
            print(prgress,val)

    def user_selects_home_owner_as_yes(self):
        self.driver.find_element(*DcprPage.home_owner_yes).click()
    
    def user_clicks_on_next_on_home_owner_page(self):
        self.driver.find_element(*DcprPage.next_on_home_owner_page).click()

    def user_clicks_on_enter_debt(self):
        self.driver.find_element(*DcprPage.enter_debt_details).click()

    #  debt details 
    def user_verify_progress_on_debt_details_page(self,val):
        ele=WebDriverWait(self.driver,6).until(ec.element_to_be_selected(DcprPage.progress_bar_on)).text
        print(ele,val)
        assert ele==val

    def user_verify_no_of_account_on_the_page(self,acc):
        numAcc=self.driver.find_elements(*DcprPage.numOfCards)
        assert len(numAcc)==acc

    def user_enters_first_cards_details(self,bal,apr,emi):
        self.driver.find_element(*DcprPage.balance1).send_keys(bal)
        self.driver.find_element(*DcprPage.APR1).send_keys(apr)
        self.driver.find_element(*DcprPage.monthPay1).send_keys(emi)

    def user_enters_second_cards_details(self,bal,apr,emi):
        self.driver.find_element(*DcprPage.balance2).send_keys(bal)
        self.driver.find_element(*DcprPage.APR2).send_keys(apr)
        self.driver.find_element(*DcprPage.monthPay2).send_keys(emi)
    
    def user_click_on_next_debt_details_page(self):
        self.driver.find_element(*DcprPage.next_on_debt_details_page).click()

    # debtsummary page

    def user_verify_total_debt(self,tdebt):
        debt=self.driver.find_element(*DcprPage.total_debt).text
        print(debt,tdebt)
        print(type(debt),type(tdebt))
        assert debt==tdebt

    def user_verify_comb_apr(self,tapr):
        comApr=self.driver.find_element(*DcprPage.com_apr).text
        print(comApr,tapr)
        print(type(comApr),type(tapr))
        assert comApr==tapr
    
    def user_verify_comb_emi(self,temi):
        combEmi=self.driver.find_element(*DcprPage.total_month_pay).text
        print(int(combEmi),temi)
        print(type(combEmi),type(temi))
        assert str(temi)==combEmi.strip()

    def user_clicks_on_next_debt_summary_page(self):
        self.driver.find_element(*DcprPage.next_on_debt_suammry_page).click()


    # monthly income page
    
    def user_verify_month_income_field_name(self):
        ele=WebDriverWait(self.driver,10).until(ec.presence_of_element_located(DcprPage.month_income_message)).is_displayed()
        assert ele

    def user_clicks_on_too_tip(self):
        self.driver.find_element(*DcprPage.income_tool_tip).click()

    def user_enters_month_amount_dcpr(self,val):
        self.driver.find_element(*DcprPage.income_text_box).send_keys(val)

    def user_selects_yes_for_month_payment(self):
        self.driver.find_element(*DcprPage.will_you_be_able_to_pay_yes_option).click()

    def user_clicks_on_next_month_income(self):
        self.driver.find_element(*DcprPage.next_on_debt_month_income_page).click()

    # lcation page
    def user_accespts_location_alert(self):
        alert=Alert(self.driver)
        alert.accept()

    def user_enter_zip_code(self):

        try:
            WebDriverWait(self.driver,10).until(ec.presence_of_element_located(DcprPage.no_home_value_error)).is_displayed()
        except Exception as e:
            print(e)
        try:
            WebDriverWait(self.driver,10).until(ec.element_to_be_clickable(DcprPage.zip_code_input)).send_keys(Keys.CONTROL + "a")
        except Exception as e:
            print(e)
        self.driver.find_element(*DcprPage.zip_code_input).send_keys(Keys.DELETE)
        self.driver.find_element(*DcprPage.zip_code_input).send_keys('90001')
        self.driver.find_element(*DcprPage.zip_code_input).send_keys(Keys.RETURN)
        

    def user_continue_with_zip_code_value(self):
        try:
            WebDriverWait(self.driver,10).until(ec.element_to_be_clickable(DcprPage.continue_with_zip_code)).click()
        except Exception as e:
            print(e)
        

    def user_clicks_on_next_on_location_page(self):
        self.driver.find_element(*DcprPage.location_page_next).click()

    #  mortgage amount

    def user_enters_mortgage_amount(self):
        self.driver.find_element(*DcprPage.mortgage_amount).send_keys(50000)

    def user_enters_mortgage_apr(self):
        self.driver.find_element(*DcprPage.mortgage_apr).send_keys(17)

    def user_selects_mortgage_year(self):
        self.driver.find_element(*DcprPage.mortgage_year).click()

    def user_selects_mortgage_year_from_drop_down(self):
        try:
            WebDriverWait(self.driver,10).until(ec.element_to_be_clickable(DcprPage.mortgage_year)).send_keys(1985)
        except Exception as e:
            print(e)

    def user_selects_term_from_the_drop_down(self):
        self.driver.find_element(*DcprPage.mortgage_term).click()
        WebDriverWait(self.driver,10).until(ec.presence_of_element_located(DcprPage.term_in_drop_down)).click()

    def user_clicks_on_next_on_mortgage_page(self):
        self.driver.find_element(*DcprPage.next_on_mortgage_page).click()

    # reco page

    def user_verify_lender_listing_on_reco(self):
        self.driver.find_element(*DcprPage.lender_listing).is_displayed()

    
        






    


        



        
        


    
    

    


    #  run for tearing down

    def browserClose(self):
        self.driver.quit()