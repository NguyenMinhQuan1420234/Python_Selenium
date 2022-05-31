from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By



chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.maximize_window()

driver.get("https://tiki.vn/")

titles = driver.find_elements(By.XPATH,'//a[@data-view-id="home_quicklinks_tab_item"]')

time.sleep(5)

for item in titles:
    item.location_once_scrolled_into_view
    print(item.text) 
    time.sleep(1)

time.sleep(5)
