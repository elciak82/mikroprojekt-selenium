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

//zmienić na GIVEN WHEN THAN Metoda BDD
url = 'https://zrabatowani.pl/'
logo_css = 'logo-top '
registration_css = 'no_p'
name_field_css = 'register_profile_name'
email_field_css = 'register_email'
password_field_css = 'register_password'
checkbox_css = 'checkbox-label'
register_button_css ='register-submit'
invalid_info = 'list-unstyled'

valid_name = 'Agnieszka'
valid_email = 'zenek3@gmail.com'
valid_email2 = 'zenek@o2.com'
invalid_email = 'zenek@ccc'
valid_password = 'zenek1234'
invalid_password = '123'

class ZrabatowaniRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        sleep(1)
        self.driver.maximize_window()
        self.driver.get(url)

    # def test1_correct_registration(self):
    #     driver = self.driver
    #     print('***TEST 1 - CORRECT REGISTRATION***')
    #
    #     logo = driver.find_element_by_class_name(logo_css)
    #     driver.implicitly_wait(3)
    #     logo.is_displayed()
    #     print ('Logo Zrabatowani was displayed.')
    #
    #     register_button = driver.find_element_by_class_name(registration_css)
    #     register_button.click()
    #     print ('Registration page was opened.')
    #
    #     user_name = driver.find_element_by_id(name_field_css)
    #     user_name.send_keys(valid_name)
    #     user_email = driver.find_element_by_id(email_field_css)
    #     user_email.send_keys(valid_email)
    #     user_password = driver.find_element_by_id(password_field_css)
    #     user_password.send_keys(valid_password)
    #     print ('All fields were filled.')
    #
    #     checkbox = driver.find_element_by_class_name(checkbox_css)
    #     checkbox.click()
    #     print('Checkbox was checked.')
    #
    #     register_button = driver.find_element_by_class_name(register_button_css)
    #     register_button.click()
    #     print ('Registed button was clicked.')
    #
    #     WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element((By.ID,'thankyou'), 'Gratulacje'))
    #     print ('User was registered correctly.')

    def test2_incorrect_invalid_mail(self):
        driver = self.driver
        print('***TEST 2 - INCORRECT REGISTRATION - INVALID EMAIL***')

        logo = driver.find_element_by_class_name(logo_css)
        driver.implicitly_wait(3)
        logo.is_displayed()
        print ('Logo Zrabatowani was displayed.')

        register_button = driver.find_element_by_class_name(registration_css)
        register_button.click()
        print ('Registration page was opened.')

        user_name = driver.find_element_by_id(name_field_css)
        user_name.send_keys(valid_name)
        user_email = driver.find_element_by_id(email_field_css)
        user_email.send_keys(invalid_email)
        user_password = driver.find_element_by_id(password_field_css)
        user_password.send_keys(valid_password)
        print ('All fields were filled.')

        checkbox = driver.find_element_by_class_name(checkbox_css)
        checkbox.click()
        print('Checkbox was checked.')

        register_button = driver.find_element_by_class_name(register_button_css)
        register_button.click()
        print ('Registered button was clicked.')

        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, invalid_info), ('"'+invalid_email+'" nie jest poprawnym adresem e-mail.')))
        print ('Info about invalid email.')

    def test3_incorrect_invalid_password(self):
        driver = self.driver
        print('***TEST 3 - INCORRECT REGISTRATION - INVALID PASSWORD***')

        logo = driver.find_element_by_class_name(logo_css)
        driver.implicitly_wait(3)
        logo.is_displayed()
        print ('Logo Zrabatowani was displayed.')

        register_button = driver.find_element_by_class_name(registration_css)
        register_button.click()
        print ('Registration page was opened.')

        user_name = driver.find_element_by_id(name_field_css)
        user_name.send_keys(valid_name)
        user_email = driver.find_element_by_id(email_field_css)
        user_email.send_keys(valid_email2)
        user_password = driver.find_element_by_id(password_field_css)
        user_password.send_keys(invalid_password)
        print ('All fields were filled.')

        checkbox = driver.find_element_by_class_name(checkbox_css)
        checkbox.click()
        print('Checkbox was checked.')

        register_button = driver.find_element_by_class_name(register_button_css)
        register_button.click()
        print ('Register button was clicked.')

        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, invalid_info), ('Podane hasło jest za krótkie. Wymyśl silniejsze hasło.')))
        print ('Info about invalid password.')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main
    # (verbosity = 0)
