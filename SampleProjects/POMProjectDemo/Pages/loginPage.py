from SampleProjects.POMProjectDemo.Locators.locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        # self.username_textbox_id = 'txtUsername'
        # self.password_textbox_id = 'txtPassword'
        # self.login_buttton_textbox_id = 'btnLogin'
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_buttton_textbox_id = Locators.login_buttton_textbox_id
        # self.invalidUsername_message_xpath = "//span[@id='spanMessage']"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_buttton_textbox_id).click()

    # def check_invalid_sername_message(self, message):
