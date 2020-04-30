from SampleProjects.POMProjectDemo.Locators.locators import Locators
class HomePage():
    def __init__(self, driver):
        self.driver = driver
        # self.welcome_link_id = 'welcome'
        # self.logout_link_text = 'Logout'
        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_text = Locators.logout_link_text


    def click_welcone(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_text).click()




