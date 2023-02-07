import time

import pytest
from UserObject.Login import login_Page
class Test_2():
    baseURL = "https://develop.d1b6r88mu92xay.amplifyapp.com/auth/signup/"
    Email = "shah1@yopmail.com"
    Password = "Zeeshan12#"
    confirm_Password = "Zeeshan12#"
    tp_code="1234"

    # @pytest.mark.skip(reason="I do not want to run this test case")
    def testsign_form(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.obj = login_Page(self.driver)
        time.sleep(3)
        self.driver.obj.setuserEmail(self.Email)
        self.driver.obj.setPassword(self.Password)
        self.driver.obj.setConfirm_Password(self.confirm_Password)
        self.driver.obj.click_started_button()
        time.sleep(2)
        self.driver.obj.Otp_code(self.tp_code)


