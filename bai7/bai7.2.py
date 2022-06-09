from optparse import Option
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument("log-level=3")

driver = Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.get("https://courses.letskodeit.com/practice")
# print(driver.title)

driver.implicitly_wait(5)

driver.find_element(By.ID,'openwindow').click()

driver.switch_to.window(driver.window_handles[1])
# print(driver.title)

# for i in driver.window_handles[0]:
#     print(i.title)

driver.find_element(By.XPATH,'//select[@name="categories"]').click()
driver.find_element(By.XPATH,'//option[@value="2022"]').click()

WebDriverWait(driver,10).until_not(EC.visibility_of_element_located((By.XPATH,'//h4[contains(text(),"JavaScript for beginners")]')))

courseTitle = driver.find_element(By.XPATH,'//h4[@class="dynamic-heading"]')
print(courseTitle.text)