from selenium import webdriver
import time
import HtmlTestRunner
import unittest


from SampleProjects.POMProjectDemo.Pages.loginPage import LoginPage
from SampleProjects.POMProjectDemo.Pages.HomePage import HomePage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/home/ronen/MyNewWork/my_selenium/drivers/chromedriver')
        # driver.implicit_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        login =LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()
        homepage = HomePage(driver)
        homepage.click_welcone()
        time.sleep(2)
        homepage.click_logout()

    def test_login_invalid_username(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        login =LoginPage(driver)
        login.enter_username('Admin1')
        login.enter_password('admin123')
        login.click_login()


# self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        # self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        # time.sleep(2)
        # self.driver.find_element_by_id('btnLogin').click()
        # time.sleep(2)
        # self.driver.find_element_by_id('welcome').click()
        # time.sleep(2)
        # self.driver.find_element_by_link_text('Logout').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')


# with this can run from command line w/o -m unittest
# Note - failed to run HTMLTestRunner from pycharm - only from command line
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/ronen/MyNewWork/my_selenium/SampleProjects/POMProjectDemo/reports'))

