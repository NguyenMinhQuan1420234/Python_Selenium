from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
        self.txtEmail = (By.XPATH,'//input[@id="email"]')
        self.txtPassword = (By.ID,'passwd')
        self.signInBtn = (By.ID,'SubmitLogin')
        
    def openLoginPage(self):
        self.driver.get(self.url)

    def getTxtEmail(self):
        return self.driver.find_element(*self.txtEmail)

    def inputTxtEmail(self, value):
        self.getTxtEmail().send_keys(value)
    
    def getTxtPassword(self):
        return self.driver.find_element(*self.txtPassword)

    def inputTxtPassword(self, value):
        self.getTxtPassword().send_keys(value)

    def clickSignInBtn(self):
        return self.driver.find_element(*self.signInBtn).click()

