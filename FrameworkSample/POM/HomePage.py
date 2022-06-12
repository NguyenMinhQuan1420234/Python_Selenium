from selenium.webdriver.common.by import By

class HomePage(object):
    def __init__(self,driver):
        self.driver = driver
        self.url = "http://automationpractice.com/index.php"
        self.title = "My Store"
        self.btnSignIn = (By.CLASS_NAME, "login")
        self.lnkBestSeller = (By.XPATH, "//a[@title='Best sellers']")
    
    def openHomePage(self):
        self.driver.get(self.url)
    
    def getBtnSignInElement(self):
        return self.driver.find_element(*self.btnSignIn)
    
    def clickSignInButton(self):
        self.getBtnSignInElement().click()
    

    def getLnkBestSeller(self):
        return self.driver.find_element(*self.lnkBestSeller)
    
    def clickLnkBestSeller(self):
        self.getLnkBestSeller().click()