from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument("log-level=3")

driver = Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.implicitly_wait(5)

action = ActionChains(driver)

doubleClick = driver.find_element(By.ID,'double-click')

action.move_to_element(doubleClick)
action.double_click(doubleClick)
action.perform()

alert = driver.switch_to.alert
print(alert.text)
