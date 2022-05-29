from selenium.webdriver  import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver = Chrome(executable_path="./bai3/chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.facebook.com/")

driver.maximize_window()

txtUsername = driver.find_element_by_xpath('//*[@id="email"]')
# txtUsername = driver.find_element(By.ID, "email")
time.sleep(2)
txtUsername.send_keys("abc@gmail.com")

txtPass = driver.find_element_by_xpath('//*[@placeholder="Password"]')
time.sleep(2)
txtPass.send_keys("123")

Login_button = driver.find_element_by_xpath('//*[@name="login"]')
Login_button.click()

error_box = driver.find_element_by_xpath('//*[@id="error_box"]/div[1]')
print(error_box.text)
error_box = driver.find_element_by_xpath('//*[@id="error_box"]/div[2]')
print(error_box.text)

error_box = driver.find_elements_by_xpath('//*[@id="error_box"]')
print(error_box[0].text)


time.sleep(5)

