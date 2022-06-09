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
chrome_options.add_argument('log-level=3')
driver = Chrome(service = Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.facebook.com/")

# driver.find_element(By.XPATH,'//a[@class="login"]').click()

driver.implicitly_wait(5)

email = driver.find_element(By.ID,'email')
email.send_keys("asdkasndl@haha.com")
password = driver.find_element(By.ID,'pass')
password.send_keys("Nono")

password.submit()

Error_message = driver.find_element(By.XPATH,'//div[@class="_9ay7"]')
print(Error_message.text)