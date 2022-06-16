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
    
    def test_verify(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach",True)
        chrome_options.add_argument("log-level=3")
        self.driver = Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        self.driver.implicitly_wait(10)
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
        
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'(//img[@title="Printed Summer Dress"])[1]')))
        self.driver.maximize_window()
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[@title="Add to cart"][@data-id-product="5"]')))
        actions = ActionChains(self.driver)
        # summerDress = self.driver.find_element(By.XPATH,'(//a[@class="button ajax_add_to_cart_button btn btn-default"])[1]')
        summerDress = self.driver.find_element(By.XPATH,'(//ul[@class="product_list grid row"]//div[@class="product-container"])[1]')
        actions.move_to_element(summerDress)
        AddToCart = self.driver.find_element(By.XPATH,'(//a[@title="Add to cart"])[1]')
        actions.click(AddToCart)
        # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//span[@title="Continue shopping"]')))
        actions.perform()
        # continueShopping = self.driver.find_element(By.XPATH,'//span[@title="Continue shopping"]')
        continueShopping = self.driver.find_element(By.CLASS_NAME,'continue')
        continueShopping.click()
        # actions.perform()
        # self.driver.find_element(By.XPATH,'//a[@title="Add to cart"][@data-id-product="5"]')
        productQuantity = self.driver.find_element(By.XPATH,'//span[@class="ajax_cart_quantity unvisible"]')
        print(productQuantity.text)
        self.assertEqual(productQuantity.text,'1')


if __name__ == '__main__':
    unittest.main()