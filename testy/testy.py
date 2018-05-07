# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
from time import sleep

url = 'https://zrabatowani.pl/'
logo_css = 'logo-top'
registration_css = 'no_p'
name_field_css = 'register_profile_name'
email_field_css = 'register_email'
password_field_css = 'register_password'
checkbox_css = 'checkbox-label'
register_button_css ='register-submit'
invalid_info = 'list-unstyled'
alert_css = 'alert-danger'

valid_name = 'Agnieszka'
valid_email = 'Agnieszka15@gmail.com'
valid_email2 = 'Agnieszka@o2.com'
invalid_email = 'Agnieszka@ccc'
valid_password = 'Agnieszka1234'
invalid_password = '123'

class ZrabatowaniRegistration(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def setUp(self):
        self.driver.maximize_window()
        register_button = self.driver.find_element_by_class_name(registration_css)
        register_button.click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, logo_css)))

    def test1_invalid_mail(self):
        driver = self.driver
        print("\n"+'***TEST 1 - INCORRECT REGISTRATION - INVALID EMAIL***')
        user_name = driver.find_element_by_id(name_field_css)
        user_name.send_keys(valid_name)
        user_email = driver.find_element_by_id(email_field_css)
        user_email.send_keys(invalid_email)
        user_password = driver.find_element_by_id(password_field_css)
        user_password.send_keys(valid_password)
        checkbox = driver.find_element_by_class_name(checkbox_css)
        checkbox.click()
        register_button = driver.find_element_by_class_name(register_button_css)
        register_button.click()
        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, invalid_info), ('"'+invalid_email+'" nie jest poprawnym adresem e-mail.')))

    def test2_invalid_password(self):
        driver = self.driver
        print("\n"+'***TEST 2 - INCORRECT REGISTRATION - INVALID PASSWORD***')
        user_name = driver.find_element_by_id(name_field_css)
        user_name.send_keys(valid_name)
        user_email = driver.find_element_by_id(email_field_css)
        user_email.send_keys(valid_email2)
        user_password = driver.find_element_by_id(password_field_css)
        user_password.send_keys(invalid_password)
        checkbox = driver.find_element_by_class_name(checkbox_css)
        checkbox.click()
        register_button = driver.find_element_by_class_name(register_button_css)
        register_button.click()
        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, invalid_info), ('Podane hasło jest za krótkie. Wymyśl silniejsze hasło.')))

    # def test3_correct_registration(self):
        # driver = self.driver
        # print("\n" + '***TEST 3 - CORRECT REGISTRATION***')
        # user_name = driver.find_element_by_id(name_field_css)
        # user_name.send_keys(valid_name)
        # user_email = driver.find_element_by_id(email_field_css)
        # user_email.send_keys(valid_email)
        # user_password = driver.find_element_by_id(password_field_css)
        # user_password.send_keys(valid_password)
        # checkbox = driver.find_element_by_class_name(checkbox_css)
        # checkbox.click()
        # register_button = driver.find_element_by_class_name(register_button_css)
        # register_button.click()
        # try:
            # WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID,'thankyou'), 'Gratulacje'))
        # except Exception:
            # driver.find_element_by_class_name(alert_css)
            # self.fail("Email has already exist in a database!")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
