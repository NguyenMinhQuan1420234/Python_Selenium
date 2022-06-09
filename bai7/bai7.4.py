from optparse import Option
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument("log-level=3")

driver = Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.get("http://demo.guru99.com/test/delete_customer.php")
driver.implicitly_wait(5)

cusID = driver.find_element(By.XPATH,'//input[@name="cusid"]')
cusID.send_keys("12345")
driver.find_element(By.XPATH,'//input[@type="submit"]').click()

# alert1 = Alert(driver)
# alert1 = driver.switch_to.alert
# print(alert1.text)
# alert1.accept()
try:
    alert1 = driver.switch_to.alert
    WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Do you really want to delete this Customer?')
    print(alert1.text)
    alert1.accept()
    
except:
    print("no alert")

WebDriverWait(driver,10).until(EC.alert_is_present())

alert2 = driver.switch_to.alert
print(alert2.text)
