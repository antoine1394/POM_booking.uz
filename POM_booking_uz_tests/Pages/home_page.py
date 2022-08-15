from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.user_cabinet_button_xpath = "/html/body/header/div/nav[2]/div[6]/a"
        self.logout_button_xpath = "/html/body/header/div/nav[2]/div[6]/div/input"
        self.username_css_selector = "body > header > div > nav.uz-menu > div.auth > a"
        self.auth_menu_xpath = "/html/body/header/div/nav[2]/div[6]/div"

    def get_auth_menu_headings(self, driver):
        actions = ActionChains(driver)
        user_cabinet_button = driver.find_element(By.XPATH, self.user_cabinet_button_xpath)
        actions.move_to_element(to_element=user_cabinet_button).perform()
        auth_menu_headings = (self.driver.find_element(By.XPATH, self.auth_menu_xpath)).text
        return auth_menu_headings

    def get_username(self, driver):
        username = (self.driver.find_element(By.CSS_SELECTOR, self.username_css_selector)).text
        return username









