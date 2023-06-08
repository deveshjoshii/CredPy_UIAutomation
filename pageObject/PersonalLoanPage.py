import time

# from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PersonalLoan:

    def __init__(self,driver):
        self.driver=driver

    #this would handle CTAs and Links
    #cpl landing page
    cpl_icon_on_homePage=(By.XPATH,"//div[@class='productIcons']//div[@class='item'][1]")
    cpl_loan_purpose=(By.XPATH,"//div[contains(@class,'ManageDebtGridPL')]//button[@id]")
    cpl_did_not_find_options=(By.XPATH,"//u[contains(text(),'Didn’t find your option?')]")
    cpl_loan_purpose_next_button=(By.ID,"nextStep")
    cpl_loan_purpose_drop_down=(By.XPATH,"//input[@id='combo-box-demo']")
    cpl_loan_purpose_back_button=(By.XPATH,"//u[text()='Back']")

    # loan details page
    cpl_how_much_loan_text =(By.NAME,"loanAmount")
    cpl_how_long_term_drpdown_values=(By.XPATH,"//div//ul[contains(@class,'MuiMenu')]//li")
    cpl_term_drop_down=(By.ID,"select-mortgageYear")
    cpl_loan_details_next_button = (By.XPATH,"//div[contains(@class,'DesktopNextBackButtons')]//button[@id='next']")
    cpl_loan_details_error_msg=(By.XPATH,"//p[contains(@class,'error') and text()='Required field']")
    cpl_loan_details_back_button=(By.ID,"back")

    # State page

    cpl_state_drop_down=(By.ID,"combo-box-demo")
    cpl_location_page_next=(By.ID,"next")

    #credit prefrence
    cpl_credit_prefrence=(By.XPATH,"//div[contains(@class,'CreditScorePrefs')]//button//h1")
    cpl_select_credit_error=(By.XPATH,"//div[contains(text(),'Please select your credit score.')]")
    cpl_credit_page_next=(By.ID,"next")

    # monthly income
    cpl_month_next_button=(By.ID,"next")
    cpl_month_income_error=(By.XPATH,"//div[contains(@class,'InfoPopup')]//div[@class='close']")
    cpl_month_income_text=(By.XPATH,"//h1[contains(text(),'What is your monthly income?')]")
    cpl_monthly_income_input_box=(By.XPATH,"//input[contains(@name,'monthlyIncome')]")
    cpl_month_tool_tip_icon=(By.XPATH,"//div[@class='popupWrapper']")
    cpl_month_tool_tip_pop_up=(By.XPATH,"//div[contains(@class,'InfoPopup')]")
    cpl_tool_tip_close_btn=(By.XPATH,"//div[contains(@class,'InfoPopup')]//div[@class='close']")

    # CPLrecomandation page

    cpl_advertiser_disclosure_link_on_reco_page=(By.XPATH,"//div[@class='container']//div[text()='Advertiser Disclosure']")
    cpl_advertiser_disclosure_pop_up_on_reco_page=(By.XPATH,"//a[contains(@href,'/advertiser-disclosure')]")
    cpl_advertiser_disclosure_close_button_on_reco_page=(By.XPATH,"//div[@class='close']")
    cpl_loan_purpose_on_reco_page=(By.XPATH,"//h1[contains(@class,'loanTitle')]//input[@name='creditScore']")
    cpl_loan_amount_on_reco_page=(By.ID,"loanAmount")
    cpl_state_on_reco_page=(By.ID,"combo-box-demo")
    cpl_loan_term_on_reco_page=(By.XPATH,"//input[@name='loanTerm']")
    cpl_loan_credit_score_on_reco_page=(By.XPATH,"//div[contains(@class,'userInput')]//div[@id='creditScore']")
    # fetch lender list
    cpl_lender_list_on_reco_page=(By.XPATH,"//h1[@id='lenderName']")


    #these will cover assertions===================

    cpl_error_on_loan_purpose=(By.XPATH,"//div[contains(text(),'Please select one option')]")
    cpl_progress_bar=(By.XPATH,"//div[contains(@class,'CommonProgressBar')]//span")
    cpl_error_on_state = (By.XPATH, "//p[@id='combo-box-demo-helper-text']")
    cpl_hows_credit_score_text=(By.XPATH,"//div[contains(@class,'credit-score-details')]//h3[contains(text(),'your credit score these days?')]")



    # Common methods

    def user_clicks_on_cpl_homepage(self):
        self.driver.find_element(*PersonalLoan.cpl_icon_on_homePage).click()





    def user_click_on_next_button(self):
        self.driver.find_element(*PersonalLoan.cpl_loan_purpose_next_button).click()

    def user_assert_error_message(self):
        self.driver.find_element(*PersonalLoan.cpl_error_on_loan_purpose).is_displayed()

    def user_fetch_loan_purpose(self):
        check=self.driver.find_elements(*PersonalLoan.cpl_loan_purpose)
        for i in check:
            try:
                i.click()
                print("clickable")
            except:
                print('not clickable')

    def user_selects_loan_purpose(self,purpose):
        check = self.driver.find_elements(*PersonalLoan.cpl_loan_purpose)
        for i in check:
            if i.get_attribute("id") in purpose:
                i.click()

    def user_click_on_did_not_find_option(self):
        self.driver.find_element(*PersonalLoan.cpl_did_not_find_options).click()

    def user_assert_on_loan_purpose_drop_down(self):
        self.driver.find_element(*PersonalLoan.cpl_loan_purpose_drop_down).is_displayed()


    # loan details page

    def user_assert_progress_bar(self,value):
        self.driver.find_element(*PersonalLoan.cpl_progress_bar)


    def user_assert_error_on_loan_details_page(self):
        self.driver.find_element(*PersonalLoan.cpl_loan_details_error_msg).is_displayed()

    def user_enter_loan_amount(self,amount):
        self.driver.find_element(*PersonalLoan.cpl_how_much_loan_text).clear()
        self.driver.find_element(*PersonalLoan.cpl_how_much_loan_text).send_keys(amount)

    def user_open_term_drop_down(self):
        self.driver.find_element(*PersonalLoan.cpl_term_drop_down).click()


    def user_selects_loan_term(self,term):
        terms=self.driver.find_elements(*PersonalLoan.cpl_how_long_term_drpdown_values)
        for i in terms:
            print(i.get_attribute("data-value"))
            if i.get_attribute("data-value")==str(term):
                i.click()
                break


    def user_clicks_on_next_on_loan_amount_page(self):

        self.driver.find_element(*PersonalLoan.cpl_loan_details_next_button).click()



    #Location page

    def user_enters_state(self,state):
        element=self.driver.find_element(*PersonalLoan.cpl_state_drop_down)
        element.send_keys(state)
        time.sleep(2)
        element.send_keys(Keys.DOWN)
        time.sleep(2)
        element.send_keys(Keys.RETURN)

    def user_click_on_next(self):
        self.driver.find_element(*PersonalLoan.cpl_location_page_next).click()

    def user_assert_error_on_state(self):
        self.driver.find_element(*PersonalLoan.cpl_error_on_state).is_displayed()

    # creditPrefrence

    def user_click_on_next_on_credit_score(self):
        self.driver.find_element(*PersonalLoan.cpl_credit_page_next).click()

    def user_assert_error_on_credit_page(self):
        self.driver.find_element(*PersonalLoan.cpl_select_credit_error).is_displayed()

    def user_fetch_all_the_credit_score(self,score_list):
        credit_score=self.driver.find_elements(*PersonalLoan.cpl_credit_prefrence)
        assert len(credit_score)==4
        for i in credit_score:
            assert i.text in score_list
            i.click()

    def user_select_credit_prefrence(self,prefrence):
        credit_score = self.driver.find_elements(*PersonalLoan.cpl_credit_prefrence)
        for i in credit_score:
            if i.text==prefrence:
                i.click()

    #  monthly income

    def user_click_on_income_next_button(self):
        self.driver.refresh()
        self.driver.find_element(*PersonalLoan.cpl_month_next_button).click()

    def user_assert_error_message_on_month(self):
        self.driver.find_element(*PersonalLoan.cpl_month_income_error).is_displayed()

    def user_assert_monthly_income_message(self):
        self.driver.find_element(*PersonalLoan.cpl_month_income_text).is_displayed()

    def user_click_on_tool_tip(self):
        self.driver.find_element(*PersonalLoan.cpl_month_tool_tip_icon).click()


    def user_assert_tool_tip_pop_up(self):
        self.driver.find_element(*PersonalLoan.cpl_month_tool_tip_pop_up).click()

    def user_close_tool_tip(self):
        self.driver.find_element(*PersonalLoan.cpl_tool_tip_close_btn).click()

    def user_enter_monthly_amout(self,income):
        self.driver.find_element(*PersonalLoan.cpl_monthly_income_input_box).send_keys(income)


    #  recomandation page

    def user_open_advertiser_disclosure(self):
        self.driver.find_element(*PersonalLoan.cpl_advertiser_disclosure_link_on_reco_page).click()

    def user_assert_link_in_the_advertiser_content(self):
        self.driver.find_element(*PersonalLoan.cpl_advertiser_disclosure_pop_up_on_reco_page).is_displayed()

    def user_close_advertiser_disclosure_pop_up(self):
        self.driver.find_element(*PersonalLoan.cpl_advertiser_disclosure_close_button_on_reco_page).click()

    def user_assert_loan_purpose(self,expected):
        purpose=self.driver.find_element(*PersonalLoan.cpl_loan_purpose_on_reco_page).get_attribute("value")
        print(purpose)
        assert (purpose==expected)

    def user_assert_loan_amount(self,loan_amount):
        amount=self.driver.find_element(*PersonalLoan.cpl_loan_amount_on_reco_page).get_attribute("value")
        repS = amount.replace("$", "")
        repS1 = repS.replace(",", "")
        print(repS1)
        print(loan_amount,"coming from reco",repS1)
        assert(repS1==str(loan_amount))

    def user_assert_loan_term(self,loan_term):
        term=self.driver.find_element(*PersonalLoan.cpl_loan_term_on_reco_page).get_attribute("value")
        print(loan_term,"coming from reco",term)
        assert(str(loan_term)==term)

    def user_assert_credit_score(self,credit_score):
        score=self.driver.find_element(*PersonalLoan.cpl_loan_credit_score_on_reco_page).text
        print(score)
        textScore=credit_score.split(" ")
        # print(credit_score,"coming from reco",textScore[0])
        assert(textScore[0]==score)

    def user_assert_lender_list(self,expected_list,lender_count):
        lender_list=self.driver.find_elements(*PersonalLoan.cpl_lender_list_on_reco_page)
        len_lst=[]
        for i in lender_list:
            len_lst.append(i.text)
        print(len_lst)
        print(len(len_lst),lender_count)
        assert len(len_lst)==lender_count
        for i in len_lst:
            if i in expected_list:
                assert True














    def browserClose(self):
        self.driver.quit()











