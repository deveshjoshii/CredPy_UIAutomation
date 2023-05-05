import time

import pytest
from pageObject.widgetPages import Widget_Page_Object

from testData.widgetData import Widget_data
from utilities.base import Base


class Test_Widget(Base):

    def test_widget(self,getdata):
        log=self.getLogger()
        widget_obj=Widget_Page_Object(self.driver)
        Base.cookie_consent(self.driver)
        widget_obj.user_validate_all_the_urls_and_validate_default_values(getdata["url"])
        log.info("wideget url")
        widget_obj.user_validate_loan_amount(getdata["loan_amount"])
        widget_obj.user_assert_loan_purpose(getdata["purpose"])
        time.sleep(3)


    @pytest.fixture(params=[Widget_data.widgetData])
    def getdata(self,request):
        return request.param




