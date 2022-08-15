from selenium import webdriver
import unittest
import time
from POM_booking_uz_tests.Pages.login_page import LoginPage
from POM_booking_uz_tests.Pages.home_page import HomePage
from POM_booking_uz_tests.Pages.test_data import Headings


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../chromedriver')

    def test_login_valid(self):
        driver = self.driver
        url = 'https://booking.uz.gov.ua/'
        self.driver.get(url)

        login = LoginPage(driver)
        login.click_authorisation_button()
        login.enter_user_email('automation_testing@i.ua')
        login.enter_password('python_selenium')
        login.click_enter_button()

        homepage = HomePage(driver)
        time.sleep(1)
        homepage.get_username(driver)
        assert homepage.get_username(driver) == 'automation_testing'
        assert homepage.get_auth_menu_headings(driver) == Headings.auth_cabinet_headings

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_login_invalid(self):
        driver = self.driver
        url = 'https://booking.uz.gov.ua/'
        self.driver.get(url)

        login = LoginPage(driver)
        login.click_authorisation_button()
        login.enter_user_email('automation_testing')  # incorrect mail
        login.enter_password('python')  # incorrect password
        login.click_enter_button()
        time.sleep(1)  # without this sleep it's impossible to get the data needed
        login.incorrect_data_popup()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
