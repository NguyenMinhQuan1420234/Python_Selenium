import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.get("htttp://www.python.org")

    def test_example(self):
        


    def tearDown(self):
        self.driver.close()