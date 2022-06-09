import unittest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class testcaseSample(unittest.TestCase):
    
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
        
        search = driver.find_element(By.XPATH,'//input[@class="search_query form-control ac_input"]')
        search.send_keys("Summer")
        search.submit()

        driver.find_element(By.XPATH,'//i[@class="icon-th-large"]').click()

        productsList = driver.find_elements(By.XPATH,'//div[@class="product-image-container"]')

        for product in productsList:
            if product.get_attribute("title") == "Printed Summer Dress":
                product.click()
                break
        WebDriverWait(driver,10).until_not(EC.presence_of_element_located((By.XPATH,'//span[@class="category-name"]')))
        
        nameOfProduct = driver.find_element(By.XPATH,'//h1[@itemprop="name"]')
        if nameOfProduct.text == "Printed Summer Dress":
            print('Product Verified!')
        else:
            print("Not what I want!")



# tester28@gmail.com    1234578
        

if __name__ == '__main__':
    unittest.main()