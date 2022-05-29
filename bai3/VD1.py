from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By
import time

# PATH = "./bai3/chromedriver.exe"
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = Chrome(executable_path=PATH)



driver.get("http://automationpractice.com/index.php")

product = driver.find_elements(By.XPATH,"//a[@class='product-name']")

for i in product:
    print(i.get_attribute("title"))