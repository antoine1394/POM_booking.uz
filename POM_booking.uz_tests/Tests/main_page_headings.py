from selenium import webdriver
import unittest
from Pages.main_page import MainPage


class MainPageTextTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/Users/macbook/Documents/DEMO_TESTS/POM_booking.uz_tests'
                                                      '/Drivers/chromedriver')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_headings_main_page(self):
        driver = self.driver
        self.driver.get('https://booking.uz.gov.ua/')

        main = MainPage(driver)
        main.get_menu_headings()
        main.get_uz_menu_headings()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')