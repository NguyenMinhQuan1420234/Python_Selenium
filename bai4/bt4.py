from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

#Using webdriver_manager to install webdriver automatically
driver = Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://www.facebook.com/")

# Forgot_button = driver.find_element(By.LINK_TEXT,"Forgotten password?").click()

driver.get("http://automationpractice.com/index.php")

driver.find_element(By.LINK_TEXT,"Sign in").click()
# Forgot_button = driver.find_element(By.LINK_TEXT,"Forgot your password?").click()
driver.find_element(By.ID, "email").send_keys("tester28@gmail.com")
driver.find_element(By.ID, "passwd").send_keys("12345678")
driver.find_element(By.ID, "SubmitLogin").click()

# driver.find_element(By.CLASS_NAME,"sfHoverForce").click()
driver.find_element(By.XPATH,'//*[@id="block_top_menu"]/ul/li[2]').click()

#mua hang
driver.find_element(By.XPATH,'//*[@id="subcategories"]/ul/li[3]/div[1]/a/img').click()
driver.find_element(By.XPATH,'//*[@id="center_column"]/ul/li[3]/div/div[2]/div[2]/a[1]/span').click()
time.sleep(5)

driver.back()

list_products = driver.find_elements(By.XPATH,'//*[@id="center_column"]/ul/li')

driver.find_element(By.XPATH,'//*[@id="center_column"]/ul/li[2]/div/div[2]/div[2]/a[1]/span').click()

time.sleep(5)

driver.find_element(By.XPATH,'//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span').click()

SoLuong = driver.find_element(By.XPATH,'//*[@id="cart_title"]/span')

print(SoLuong.text)
# //a[contains(text(),"value")]
time.sleep(5)
SKU = driver.find_elements(By.XPATH,'//small[@class="cart_ref"]')
productName = driver.find_elements(By.XPATH,'//p[@class="product-name"]')
Model = driver.find_elements(By.XPATH,'//a[contains(text(),"Color")]')
desList = driver.find_elements(By.CLASS_NAME, 'cart_description')
for i in desList:
    print(i.find_element(By.XPATH, "/p[@class = 'product-name']/a").text + "\n")
    # print(i.find_element(By.CLASS_NAME, "cart_ref").text + "\n")

    


driver.close()
