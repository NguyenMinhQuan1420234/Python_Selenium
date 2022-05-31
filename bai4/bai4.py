from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#Using webdriver_manager to install webdriver automatically
driver = Chrome(service=Service(ChromeDriverManager().install()))
# driver = Chrome(ChromeDriverManager().install())


# 1. Open this link http://automationpractice.com/index.php
driver.get("http://automationpractice.com/index.php")


# 2. Click on Sign In link
# driver.find_element(By.XPATH, "//a[@class='login']").click()
driver.find_element_by_xpath("//a[@class='login']").click()

# 3. Login to page using correct email and password
driver.find_element(By.ID, "email").send_keys("tester28@gmail.com")
driver.find_element(By.ID, "passwd").send_keys("12345678")
driver.find_element(By.ID, "SubmitLogin").click()

Name = driver.find_element(By.CLASS_NAME,"header_user_info")
print(Name.text)

# # 4. In My Account page, click MY PERSONAL INFORMATION button
# driver.find_element(By.XPATH, "//span[text()='My personal information']").click()

# # 5. Print to cmd
# print(driver.find_element(By.ID, "email").get_attribute("value"))

#  Close driver
driver.quit()