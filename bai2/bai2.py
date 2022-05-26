from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


def verifyText(Text1, Text2):
    if Text1 == Text2:
        print("True")
    else: 
        print("False")

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = Chrome(executable_path="../Python_Selenium/bai2/chromedriver.exe")

driver.maximize_window()

driver.get("https://www.google.com")
print(driver.title)

element = driver.find_element_by_name("q")
element.send_keys("vnexpress", Keys.RETURN)

element = driver.find_element_by_css_selector("#rso > div:nth-child(1) > div > div > div > div > div > div > div.yuRUbf > a")
driver.implicitly_wait(10)
element.click()
verifyText(driver.title,"VnExpress - Báo tiếng Việt nhiều người xem nhất")

driver.get("https://www.python.org/")
verifyText(driver.title,"Python.org")


if "Python.org" in driver.title:
    print("Co chuoi")
    
verifyText(driver.title,"Welcome to Python.org")
# print(driver.title)

# driver.back()
# print(driver.current_url)
# driver.forward()
# print(driver.page_source)



time.sleep(5)

driver.close()
