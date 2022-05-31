from tabnanny import check
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = Chrome(ChromeDriverManager().install(),options=chrome_options)
# driver.get("https://www.facebook.com")

# username = driver.find_element(By.ID,"email")
# password = driver.find_element(By.ID,"pass")

# print(username.is_displayed())
# print(password.is_displayed())

# print(username.is_enabled())
# print(password.is_enabled())

# print(username.is_selected())
# print(password.is_selected())

# driver.get("https://courses.letskodeit.com/practice")

# textbox = driver.find_element(By.ID,'displayed-text')
# hide = driver.find_element(By.ID,'hide-textbox').click()
# checkbox1 = driver.find_element(By.ID,'bmwcheck')
# checkbox2 = driver.find_element(By.ID,'benzcheck')
# checkbox2.click()


# print(textbox.is_displayed())
# print(textbox.is_enabled())

# print("BMW check: ", checkbox1.is_selected())
# print("BENZ check: ", checkbox2.is_selected())

# radioBTN1 = driver.find_element(By.ID,'bmwradio')
# print("BMW check: ", radioBTN1.is_selected())
# radioBTN1.click()
# print("BMW check: ", radioBTN1.is_selected())

# driver.get("http://the-internet.herokuapp.com/checkboxes")

# checkbox_list = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')

# # if checkbox_list[0].is_selected() == False:
# #     checkbox_list[0].click()

# # if checkbox_list[1].is_selected() == True:
# #     checkbox_list[1].click()

# for checkbox in checkbox_list:
#     if not checkbox.is_selected():
#         checkbox.click()
#         print(checkbox.is_selected())
#     else:
#         checkbox.click()
#         print(checkbox.is_selected())

# print(checkbox_list[0].is_selected())
# print(checkbox_list[1].is_selected())
driver.get("https://courses.letskodeit.com/practice")

driver.find_element(By.ID,'hide-textbox').click()

# driver.find_element(By.ID,'displayed-text').send_keys("abc")
textbox = driver.find_element(By.ID, "displayed-text")
textbox.location_once_scrolled_into_view

driver.execute_script("arguments[0].value = 'setHide' ", textbox)
driver.execute_script("arguments[0].click() ", textbox)

time.sleep(3)

driver.find_element(By.ID,'show-textbox').click()

time.sleep(5)

driver.close()