from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def item_text(item):
    return driver.find_element(By.XPATH,f"//div[contains(@class,'ie3A+n bM+7UW Cve6sh')][text()='{item}']")

def item_list(list):
    return driver.find_elements(By.XPATH,f"//div[contains(@class,'ie3A+n bM+7UW Cve6sh')][contains(text(),'{list}')]")
    
# return driver.find_element(By.XPATH,f"//div[contains(@class,'ie3A+n bM+7UW Cve6sh')][text()='{item}']")
# //div[contains(@class,'ie3A+n bM+7UW Cve6sh')][text()='[Mã ELAP500K giảm 8% đơn 500K] Apple iPhone 11 128GB']

# driver.find_element_by_xpath("//option[@value='" + state + "']").click()


driver = Chrome(service = Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://shopee.vn/")

search_bar = driver.find_element(By.XPATH,'//input[@class="shopee-searchbar-input__input"]')
time.sleep(5)

search_bar.send_keys("iphone")
search_bar.send_keys(Keys.ENTER)

time.sleep(5)
#class="row shopee-search-item-result__items"
# productList = driver.find_elements(By.XPATH,'//div[contains(@class,"ie3A+n bM+7UW Cve6sh")]')


# item_text("[Mã ELAP500K giảm 8% đơn 500K] Apple iPhone 11 128GB").click()

# time.sleep(5)

# class="col-xs-2-4 shopee-search-item-result__item" -> class of items of shop
item_list = driver.find_elements(By.XPATH,'//div[@class="col-xs-2-4 shopee-search-item-result__item"]')

print(item_list[0].text)

time.sleep(5)

# for item in item_list('iPhone 11'):
#     item.click()
#     time.sleep(5)
#     driver.back()
#     time.sleep(5)

# item = driver.find_element(By.XPATH,"//div[contains(@class,"ie3A+n bM+7UW Cve6sh")]")


# //div[contains(@class,"ie3A+n bM+7UW Cve6sh")]
#//img[contains(@alt,"iPhone 11")] Iphone 11 :V


# for i in productList:
#     i.find_element('//img[contains(@alt,"iPhone 11")]').click()

# //a[contains(text(),"value")]

time.sleep(5)

driver.close()