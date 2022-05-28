from telnetlib import EC
import unittest
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

class PageMyStore(unittest.TestCase):
    def setUp(self):
        # Create webdriver instance
        self.driver = webdriver.Chrome(executable_path="./bai3/chromedriver.exe")
        self.driver.implicitly_wait(5)
        #open page
        self.driver.get("http://automationpractice.com/index.php")
        self.wait = WebDriverWait(self.driver,10)
        # wait for loading page
        self.wait.until(EC.title_contains("My Store"))

    def Test_SignIn(self):
        signIn_button = self.driver.find_element_by_class_name("login")
        signIn_button.click()

        self.wait.until(EC.title_contains("Login"))

        email_input = self.driver.find_element_by_id("email")
        email_input.send_keys("uiabc@gmail.com")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__" :
    unittest.main()
    PageMyStore.setUp()
    PageMyStore.Test_SignIn()