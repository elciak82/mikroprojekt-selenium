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
cookies_button_css = 'cc-allow'
registration_css = 'no_p'
name_field_css = 'register_profile_name'
email_field_css = 'register_email'
password_field_css = 'register_password'
checkbox_css = 'checkbox-label'
register_button_css ='register-submit'
invalid_info = 'list-unstyled'
alert_css = 'alert-danger'
log_tab_css = 'dropdownLogin'
user_log_email_css = 'username'
user_log_password_css = 'password'
log_button_css = 'div[id=top-menu] button[name=_submit]'
user_check_css = 'user-welcome'

valid_name = 'Agnieszka'
valid_email = 'agula5376@gmail.com'
valid_email2 = 'Agnieszka@o2.com'
invalid_email = 'Agnieszka@ccc'
valid_password = 'AGULA5376'
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
        cookies_button = self.driver.find_element_by_class_name(cookies_button_css)
        cookies_button.click()
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

    def test3_login(self):
        driver = self.driver
        print("\n" + '***TEST 3 - CORRECT_LOGIN***')
        log_tab = driver.find_element_by_id(log_tab_css)
        log_tab.click()
        user_email = driver.find_element_by_id(user_log_email_css)
        user_email.send_keys(valid_email)
        user_password = driver.find_element_by_id(user_log_password_css)
        user_password.send_keys(valid_password)
        log_button = driver.find_element_by_css_selector(log_button_css)
        log_button.click()
        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, user_check_css), ("Witaj " + valid_name)))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
