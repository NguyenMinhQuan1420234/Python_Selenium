from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By
import time
import webbrowser
from selenium import webdriver

PATH = "C:\\Users\\banch\\Python_Selenium\\bai3\\VD\\chromedriver.exe"
# driver = Chrome(executable_path='C:\\Users\\banch\\Python_Selenium\\bai3\\VD\\chromedriver.exe')
# PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)



driver.get("http://automationpractice.com/index.php")

product = driver.find_elements(By.XPATH,"//a[@class='product-name']")

for i in product:
    print(i.get_attribute("title"))