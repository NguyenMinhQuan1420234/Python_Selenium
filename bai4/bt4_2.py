from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#Using webdriver_manager to install webdriver automatically
driver = Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://automationpractice.com/index.php")

