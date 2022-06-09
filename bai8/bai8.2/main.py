import unittest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class testcaseSample(unittest.TestCase):
    
    # def test_open_google(self):
    #     chrome_options = Options()
    #     chrome_options.add_experimental_option("detach",True)
    #     chrome_options.add_argument("log-level=3")
    #     driver = Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

    #     driver.get("http://automationpractice.com/index.php")
    #     self.assertEqual("My Store",driver.title)
    #     driver.close()

    def test_verify_account(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach",True)
        chrome_options.add_argument("log-level=3")
        driver = Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        driver.get("http://automationpractice.com/index.php")

        driver.find_element(By.XPATH,'//a[@class="login"]').click()
        email = driver.find_element(By.ID,'email')
        email.send_keys('tester28@gmail.com')
        password = driver.find_element(By.ID,'passwd')
        password.send_keys('12345678')

        driver.find_element(By.ID,'SubmitLogin').click()

        driver.implicitly_wait(5)
        
        driver.find_element(By.XPATH,'//i[@class="icon-user"]').click()
        
        check = driver.find_element(By.XPATH,'//input[@id="email"]')
        emailName = check.get_attribute("value")

        self.assertEqual(emailName,"tester28@gmail.com")
        print("Email Verified!")

# tester28@gmail.com    1234578
        

if __name__ == '__main__':
    unittest.main()
    