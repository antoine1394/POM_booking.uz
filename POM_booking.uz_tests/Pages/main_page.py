from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver

        self.menu_class_name = 'menu'
        self.uz_menu_class_name = 'uz-menu'

    def get_menu_headings(self):
        menu = self.driver.find_element(By.CLASS_NAME, self.menu_class_name)
        menu_headings_text = menu.text
        print(menu_headings_text)

    def get_uz_menu_headings(self):
        uz_menu = self.driver.find_element(By.CLASS_NAME, self.uz_menu_class_name)
        uz_menu_text = uz_menu.text
        print(uz_menu_text)


