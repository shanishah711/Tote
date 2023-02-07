import time
from selenium.webdriver.common.by import By


class login_Page():
    Email_input_field_xpath = "//*[@id='root']/div[2]/div/div/div/form/div[3]/div/input"
    Password_input_field_xpath = "//*[@id='root']/div[2]/div/div/div/form/div[4]/div/input"
    Confirm_password_input_field_xpath = "//*[@id='root']/div[2]/div/div/div/form/div[5]/div/input"
    Click_getstarted_butoon_xpath = "//*[@id='root']/div[2]/div/div/div/form/div[6]/button"
    otp_code_by_clname = "//*[@id='root']/div[2]/div/div/form/div[4]/input[1]"
    Verify_button_click_xpath="//*[@id='root']/div[2]/div/div/form/div[6]/button"

    def __init__(self, driver):
        self.driver = driver

    def setuserEmail(self, Email):
        self.driver.find_element(By.XPATH, self.Email_input_field_xpath)

        self.driver.find_element(By.XPATH, self.Email_input_field_xpath).send_keys(Email)

    def setPassword(self, Password):
        self.driver.find_element(By.XPATH, self.Password_input_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.Password_input_field_xpath).send_keys(Password)

    def setConfirm_Password(self, confirm_Password):
        password_field = self.driver.find_element(By.XPATH, self.Confirm_password_input_field_xpath)
        password_field.clear()
        self.driver.find_element(By.XPATH, self.Confirm_password_input_field_xpath).send_keys(confirm_Password)

    def click_started_button(self, ):
        self.driver.find_element(By.XPATH, self.Click_getstarted_butoon_xpath).click()

    def Otp_code(self, tp_code):
        self.driver.find_element(By.XPATH, self.otp_code_by_clname)
        self.driver.find_element(By.XPATH, self.otp_code_by_clname).click()
        self.driver.find_element(By.XPATH, self.otp_code_by_clname).send_keys(tp_code)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.otp_code_by_clname).click()




