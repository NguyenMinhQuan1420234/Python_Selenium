#Drag and Drop
from argparse import Action
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
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument("log-level=3")

driver = Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
# driver.get("https://demo.guru99.com/test/drag_drop.html")
# driver.maximize_window()
iframe =driver.find_element(By.XPATH,'//iframe[@data-src="../../demoSite/practice/droppable/photo-manager.html"]')
driver.switch_to.frame(iframe)

actions = ActionChains(driver)

driver.implicitly_wait(5)
driver.maximize_window()
images = driver.find_elements(By.XPATH,'//li[@class="ui-widget-content ui-corner-tr ui-draggable ui-draggable-handle"]')
trash = driver.find_element(By.ID,'trash')
for image in images:
    actions.drag_and_drop(image,trash)
    actions.perform()
    
# driver.close()