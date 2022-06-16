import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from ddt import ddt,unpack,data
from selenium.common.exceptions import TimeoutException


@ddt
class baitap_login(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach",True)
        chrome_options.add_argument("log-level=3")
        self.driver = Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        self.driver.get("http://automationpractice.com/index.php")
    
    def tearDown(self):
        self.driver.close()

    @data(["test12222@lo.com","12345678"],["banchi0072000@yahoo.com","12345678"], ["test12224@lo.com","12345678"])
    @unpack
    def test_Login_username_password(self, username, passw):
        self.driver.find_element(By.XPATH,'//a[@class="login"]').click()
        email = self.driver.find_element(By.ID,'email')
        email.send_keys(username)
        password = self.driver.find_element(By.ID,'passwd')
        password.send_keys(passw)

        self.driver.find_element(By.ID,'SubmitLogin').click()

        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'(//div[@class="alert alert-danger"])[1]')))
        except TimeoutException:
            self.fail("No error message appear")
        
        alert_msg = self.driver.find_element(By.XPATH,'(//div[@class="alert alert-danger"])[1]')
        # print(alert_msg.text.splitlines())
        msg = self.driver.find_element(By.XPATH,'//li[contains(text(),"Authentication failed.")]')
        self.assertIn("Authentication failed.",msg.text)
        # self.assertTrue(alert_msg.is_displayed())
        

if __name__ == '__main__':
    unittest.main()
    