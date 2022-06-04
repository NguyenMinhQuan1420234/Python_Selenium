from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument(r"user-data-dir=C:\Users\hv\AppData\Local\Google\Chrome\User Data\Default")

driver = Chrome(service=Service(ChromeDriverManager().install()), options= chrome_options)
driver.maximize_window()

driver.get("https://www.traveloka.com/vi-vn")

driver.find_element(By.XPATH,'//div[contains(text(),"Vé máy bay")][@class="css-901oao r-1h9nbw7 r-16y2uox r-1sixt3s r-1b43r93 r-majxgm r-1cwl3u0 r-fdjqy7 r-3s2u2q"]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//input[@placeholder="Origin"]').click()
driver.find_element(By.XPATH,'//span[contains(text(),"SGN - Sân bay Tân Sơn Nhất")]').click()
driver.find_element(By.XPATH,'//input[@placeholder="Destination"]').click()
driver.find_element(By.XPATH,'//span[contains(text(),"Đà Nẵng, Việt Nam")]').click()

# ngayDi = driver.find_element(By.XPATH,'//input[@aria-labelledby="depatureDate"]')
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//input[@aria-labelledby="depatureDate"]').click()
# driver.execute_script("arguments[0].value = '9 thg 6, 2022' ",ngayDi)

driver.find_element(By.XPATH,'(//div[text() = "16"])[1]').click()
# driver.execute_script("arguments[0].click()")

driver.find_element(By.XPATH,'//div[contains(text(),"Tìm chuyến bay")][@aria-hidden="true"]').click()

# flightData = WebDriverWait(driver,30).until(EC.visibility_of_all_elements_located((By.XPATH,'//div[@class="css-901oao r-1sixt3s, r-ubezar r-majxgm r-135wba7 r-aq742g r-fdjqy7"]')))
list = driver.find_elements(By.XPATH,'//div[@class="css-1dbjc4n r-kdyh1x r-da5iq2 r-184en5c"]')
TenChuyenBay = driver.find_elements(By.XPATH,'//div[@class="css-901oao r-1sixt3s r-ubezar r-majxgm r-135wba7 r-aq742g r-fdjqy7"]')
ThoiGianBay = driver.find_elements(By.XPATH,'//div[@class="css-1dbjc4n r-6koalj r-18u37iz r-mbgqwd"]')
GiaTien = driver.find_elements(By.XPATH,'//div[@class="css-901oao r-1sixt3s r-adyw6z r-b88u0q r-rjixqe r-fdjqy7"]')

for i in range(0,10):    
    print("Chuyen thu "+ str(i+1) +": "+ TenChuyenBay[i].text + "\n" + ThoiGianBay[i].text + "\n" + GiaTien[i].text)
