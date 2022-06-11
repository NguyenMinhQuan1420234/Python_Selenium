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
        email.send_keys('banchi0072000@yahoo.com')
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
        # time.sleep(20)
        iframe = driver.find_element(By.XPATH,('//iframe[@class="fancybox-iframe"]'))
        # print(isframe(iframe))
        
        driver.switch_to.frame(iframe)
        # # driver.maximize_window()
        # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//h1[@itemprop="name"]')))
        productName = driver.find_element(By.XPATH,'//h1[@itemprop="name"]')
        self.assertEqual(productName.text,"Printed Summer Dress")  # Verify name task
        
        driver.find_element(By.XPATH,'//img[@id="bigpic"]').click()

        blackDress = driver.find_element(By.XPATH,'//a[@id="color_11"]')
        color1 = blackDress.get_attribute("name")
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
        
        driver.find_element(By.ID,'new_comment_tab_btn').click()
        ReviewForm = driver.find_element(By.XPATH,'//div[@class="new_comment_form_content col-xs-12 col-sm-6"]')
        self.assertTrue(ReviewForm.is_displayed())


        driver.find_element(By.XPATH,'//a[@title="4"]').click()
        driver.find_element(By.ID,'comment_title').send_keys("Refund please!")
        driver.find_element(By.ID,'submitNewMessage').click()

        WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,'new_comment_form_error')))
        alertMsg = driver.find_element(By.ID,'new_comment_form_error')
        # EC.text_to_be_present_in_element
        self.assertEqual(alertMsg.text,"Comment is incorrect")
        comment = driver.find_element(By.ID,'content')
        comment.send_keys("Refund or die bitch!")
        driver.find_element(By.ID,'submitNewMessage').click()

        popup = driver.find_element(By.XPATH,'//div[@class="fancybox-inner"]')
        self.assertTrue(popup.is_displayed())

        driver.find_element(By.XPATH,'//button[@class="button btn-default button-medium"]').click()

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