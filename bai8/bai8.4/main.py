from inspect import isframe
import unittest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class testcaseSample(unittest.TestCase):
    
    def test_verify_account(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach",True)
        chrome_options.add_argument("log-level=3")
        driver = Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        driver.get("http://automationpractice.com/index.php")
        driver.maximize_window()

        driver.find_element(By.XPATH,'//a[@class="login"]').click()
        email = driver.find_element(By.ID,'email')
        email.send_keys('tester28@gmail.com')
        password = driver.find_element(By.ID,'passwd')
        password.send_keys('12345678')

        driver.find_element(By.ID,'SubmitLogin').click()

        driver.implicitly_wait(5)
        
        search = driver.find_element(By.XPATH,'//input[@class="search_query form-control ac_input"]')
        search.send_keys("Summer")
        search.submit()

        driver.find_element(By.XPATH,'//i[@class="icon-th-large"]').click()
        
        productsList = driver.find_elements(By.XPATH,'//div[@class="product-image-container"]')
        #//a[@title="Printed Summer Dress"]
        productsList[0].click()
        WebDriverWait(driver,20)
        time.sleep(20)
        iframe = driver.find_element(By.XPATH,('//iframe[@class="fancybox-iframe"]'))
        # print(isframe(iframe))
        
        driver.switch_to.frame(iframe)
        # # driver.maximize_window()
        # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//h1[@itemprop="name"]')))
        productName = driver.find_element(By.XPATH,'//h1[@itemprop="name"]')
        self.assertEqual(productName.text,"Printed Summer Dress")  # Verify name task
        
        driver.find_element(By.XPATH,'//img[@id="bigpic"]').click()

        colors = []

        blackDress = driver.find_element(By.XPATH,'//a[@id="color_11"]')
        colors += blackDress.get_attribute("name")
        print(colors[0])
        orangeDress = driver.find_element(By.XPATH,'//a[@id="color_13"]')
        color2 = orangeDress.get_attribute("name")
        blueDress = driver.find_element(By.XPATH,'//a[@id="color_14"]')
        color3 = blueDress.get_attribute("name")
        yellowDress = driver.find_element(By.XPATH,'//a[@id="color_16"]')
        color4 = yellowDress.get_attribute("name")
        yellowDress.click()
        
        bigPic = driver.find_element(By.XPATH,'//img[@id="bigpic"]')
        srcLink = bigPic.get_attribute("src")

        self.assertEqual(srcLink,"http://automationpractice.com/img/p/1/2/12-large_default.jpg") # Verify big Picture changed
        
        thumbNail = driver.find_element(By.XPATH,'//img[@id="thumb_12"]')
        thbNailID = thumbNail.get_attribute("id")

        self.assertEqual(thbNailID,"thumb_12") # Verify thumbnail
        



        # src="http://automationpractice.com/img/p/1/2/12-large_default.jpg" yellow dress



        # WebDriverWait(driver,10).until_not(EC.presence_of_element_located((By.XPATH,'//h1[@class="page-heading  product-listing"]')))
        
        # nameOfProduct = driver.find_element(By.XPATH,'//h1[@itemprop="name"]')
        # if nameOfProduct.text == "Printed Summer Dress":
        #     print('Product Verified!')
        # else:
        #     print("Not what I want!")



# tester28@gmail.com    1234578
        

if __name__ == '__main__':
    unittest.main()