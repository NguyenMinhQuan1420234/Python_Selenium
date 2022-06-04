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

driver = Chrome(service=Service(ChromeDriverManager().install()), options= chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationpractice.com/index.php")

driver.find_element(By.XPATH,'//a[@class="login"]').click()

driver.find_element(By.ID,'email_create').send_keys("abcdef123123@gmail.com")
driver.find_element(By.ID,'SubmitCreate').click()

# driver.implicitly_wait(10)
# driver.find_element(By.ID,'uniform-id_gender1').click()

radioMale = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.ID,'uniform-id_gender1')))
radioMale.click()