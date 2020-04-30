from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/home/ronen/MyNewWork/my_selenium/drivers/chromedriver')
        # driver.implicit_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        time.sleep(2)
        self.driver.find_element_by_id('btnLogin').click()
        time.sleep(2)
        self.driver.find_element_by_id('welcome').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('Logout').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')


# with this can run from command line w/o -m unittest
if __name__ == '__main__':
    unittest.main()

