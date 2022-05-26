from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)

search = driver.find_element_by_name("s") # chon o search dua tren name tren html
search.send_keys("test") # go~ vao test trong o search
search.send_keys(Keys.RETURN)  #Enter = RETURN

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-title")
        print(header.text)

finally:
    driver.quit()

#print(driver.page_source)
# main = driver.find_element_by_id("main")
print(main.text)

time.sleep(5)

driver.quit()
#ok