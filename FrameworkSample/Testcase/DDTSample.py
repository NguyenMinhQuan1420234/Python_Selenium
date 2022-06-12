from distutils.log import Log
import sys
sys.path.append(r"C:\Users\hv\Downloads\Python_Selenium-main\FrameworkSample")

import unittest
from ddt import ddt,unpack,data
from MyMath.MyMathModule import is_prime, plus
from POM.HomePage import HomePage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from POM.LoginPage import LoginPage
from selenium.webdriver.common.keys import Keys

@ddt
class DDTSample(unittest.TestCase):
    def setUp(self) -> None:
        chrome_options = Options()
        # Giu browser khong bi tat
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--log-level=3")

        self.driver = Chrome(service=Service(ChromeDriverManager().install()), chrome_options= chrome_options)

    # def tearDown(self) -> None:
    #     self.driver.quit()


    def testLogin(self):
        # homePage = HomePage(self.driver)
        # homePage.openHomePage()
        # homePage.clickLnkBestSeller()
        loginPage = LoginPage(self.driver)
        loginPage.openLoginPage()
        loginPage.inputTxtEmail("banchi0072000@yahoo.com")
        loginPage.inputTxtPassword("12345678")
        loginPage.clickSignInBtn()



if __name__ == '__main__':
    unittest.main()
    