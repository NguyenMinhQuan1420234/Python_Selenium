import unittest
from pip import main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from ddt import ddt,unpack,data
from selenium.common.exceptions import TimeoutException

@ddt
class auto_survey (unittest.TestCase):
    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach",True)
        chrome_options.add_argument("log-level=3")
        self.driver = Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        self.driver.get("https://forms.office.com/pages/responsepage.aspx?id=VIww9AgC00OvrR-N8vZ4t2zp7ttwIKlDi-GuPcvdCcJUN0hPM0ZMU0dGTFYxQ1pUSEFLMzM5VEJFNS4u")

    def tearDown(self):
        self.driver.close()
    
    @data (["Awesome Teacher ever !!!"],["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"])
    def test_auto_survey(self,text):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,'//div[@class="select-placeholder"]').click()
        self.driver.find_element(By.XPATH,'//div[@aria-label="Thinking method & Problem solving"]').click()
        self.driver.find_element(By.XPATH,'//div[contains(text(),"Next")]').click()

        Excellent = self.driver.find_elements(By.XPATH,'//input[@type="radio"][@value="1"]')
        for checkbox in Excellent:
            checkbox.click()

        self.driver.find_element(By.XPATH,'//input[@aria-labelledby="QuestionChoiceOption1"]').click()
        self.driver.find_element(By.XPATH,'//textarea[@placeholder="Enter your answer"]').send_keys(text)
        self.driver.find_element(By.XPATH,'(//div[@class="button-content"])[3]').click()

        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'(//span[contains(text(),"Thank you very much for your valuable comments and feedback.")])[1]')))
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()