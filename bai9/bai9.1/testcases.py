import unittest
from dotenv import main
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class TestCaseSample(unittest.TestCase):
    
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach",True)
        chrome_options.add_argument("log-level=3")
        self.driver = Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        self.driver.implicitly_wait(5)

    # def tearDown(self):
    #     self.driver.close()

    def test_verify_shoppingButtons(self):
        self.driver.get("http://automationpractice.com/index.php")

        self.driver.find_element(By.XPATH,'//a[@class="login"]').click()
        email = self.driver.find_element(By.ID,'email')
        email.send_keys('tester28@gmail.com')
        password = self.driver.find_element(By.ID,'passwd')
        password.send_keys('12345678')
        self.driver.find_element(By.ID,'SubmitLogin').click()

        search = self.driver.find_element(By.XPATH,'//input[@class="search_query form-control ac_input"]')
        search.send_keys("Summer")
        search.submit()
        
        self.driver.find_element(By.XPATH,'//i[@class="icon-th-large"]').click()

        product = self.driver.find_element(By.XPATH,'(//img[@title="Printed Summer Dress"])[1]')

        actions = ActionChains(self.driver)
        actions.move_to_element(product)

        actions.perform()

        addToCart = self.driver.find_element(By.XPATH,'//a[@title="Add to cart"][@data-id-product="5"]')
        # print(addToCart.text)
        
        # self.assertEqual(addToCart.is_displayed(),True) # verify Add to cart button

        More = self.driver.find_element(By.XPATH,'(//a[@class="button lnk_view btn btn-default"])[1]')
        # self.assertTrue(More.is_displayed())

    # def test_message_to_customer_service(self):
        
    #     self.driver.get("http://automationpractice.com/index.php")

    #     self.driver.find_element(By.XPATH,'//a[@title="Contact Us"]').click()

    #     select = Select(self.driver.find_element(By.ID,'id_contact'))
    #     select.select_by_value('2')
    #     email = self.driver.find_element(By.ID,'email')
    #     email.send_keys("tester28@gmail.com")
    #     orderReference = self.driver.find_element(By.ID,'id_order')
    #     orderReference.send_keys("269")
    #     AttachFile = self.driver.find_element(By.ID,'fileUpload')
    #     AttachFile.send_keys(r"C:\Users\hv\Downloads\work\bai8\SampleTestcase.docx")
    #     message = self.driver.find_element(By.ID,'message')
    #     message.send_keys("Your product is the worst ever!")
    #     self.driver.find_element(By.ID,'submitMessage').click()

    #     alertMsg = self.driver.find_element(By.XPATH,'//p[@class="alert alert-success"]')
    #     MsgVisible = alertMsg.is_displayed()
    #     self.assertTrue(MsgVisible)
        

if __name__ == '__main__':
    unittest.main()
    