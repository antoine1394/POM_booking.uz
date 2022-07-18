from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.authorisation_button_xpath = "/html/body/header/div/nav[2]/div[6]/a"
        self.email_textbox_xpath = "/html/body/header/div/nav[2]/div[6]/div/form/input"
        self.password_textbox_xpath = "/html/body/header/div/nav[2]/div[6]/div/form/div[2]/input"
        self.enter_button_xpath = "/html/body/header/div/nav[2]/div[6]/div/form/div[4]/button"
        self.incorrect_data_message_class_name = "popup-alert-message"
        self.popup_ok_button_xpath = "/html/body/div[8]/div[2]/div[2]/a"

    def click_authorisation_button(self):
        self.driver.find_element(By.XPATH, self.authorisation_button_xpath).click()

    def enter_user_email(self, user_email):
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).send_keys(user_email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def click_enter_button(self):
        self.driver.find_element(By.XPATH, self.enter_button_xpath).click()

    def incorrect_data_popup(self):
        popup = self.driver.find_element(By.CLASS_NAME, self.incorrect_data_message_class_name)
        actual_popup_text = popup.text
        expected_popup_text = "Логін або пароль введені невірно"
        assert actual_popup_text == expected_popup_text
        self.driver.find_element(By.XPATH, self.popup_ok_button_xpath).click()






