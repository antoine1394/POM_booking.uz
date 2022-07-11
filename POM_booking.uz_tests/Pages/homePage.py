from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.user_cabinet_button_xpath = "/html/body/header/div/nav[2]/div[6]/a"
        self.logout_button_xpath = "/html/body/header/div/nav[2]/div[6]/div/input"

    def move_to_user_cabinet(self, driver):
        actions = ActionChains(driver)
        user_cabinet_button = driver.find_element(By.XPATH, self.user_cabinet_button_xpath)
        actions.move_to_element(to_element=user_cabinet_button).perform()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()


        
