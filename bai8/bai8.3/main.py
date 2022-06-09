import unittest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class testcaseSample(unittest.TestCase):

    def test_verify_account(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach",True)
        chrome_options.add_argument("log-level=3")
        driver = Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        driver.get("https://courses.letskodeit.com/practice")

        driver.find_element(By.ID,'openwindow').click()
        WebDriverWait(driver,10).until_not(EC.presence_of_element_located((By.XPATH,'//h4[contains(text(),"JavaScript for beginners")]')))

        driver.switch_to.window(driver.window_handles[1])
        
        driver.find_element(By.XPATH,'//select[@name="categories"]').click()

        driver.find_element(By.XPATH,'//option[@value="2022"]').click()

        newCourse = driver.find_element(By.XPATH,'//div[@class="zen-course-title dynamic-text"]')
        WebDriverWait(driver,10).until(EC.staleness_of(newCourse))

        courseList = driver.find_elements(By.XPATH,'//div[@class="zen-course-title dynamic-text"]')
        # numberOfCourse = 0
        # for course in courseList:
        #     numberOfCourse+=1
        
        # index = len(courseList)

        self.assertEqual(len(courseList),1)
        print("\n There's only one Course showed \n")


# oldCourse = driver.find_element(By.XPATH,'')
# WebDriverWait(driver,10).until(EC.staleness_of(oldCourse))

# tester28@gmail.com    1234578
        

if __name__ == '__main__':
    unittest.main()
    