from selenium import webdriver
import time
import unittest
from Pages.loginPage import LoginPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/Users/macbook/Documents/DEMO_TESTS/POM_booking.uz_tests'
                                                      '/Drivers/chromedriver')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        self.driver.get('https://booking.uz.gov.ua/')

        login = LoginPage(driver)
        login.click_authorisation_button()
        login.enter_user_email('automation_testing@i.ua')
        login.enter_password('python_selenium')
        login.click_enter_button()
        time.sleep(5)