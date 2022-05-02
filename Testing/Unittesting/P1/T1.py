import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchEngine1(unittest.TestCase):

    def test_google(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\hp\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("http://www.gmail.com")
        print("The title of the page is : "+self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\hp\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("http://www.yahoo.com")
        print("The title of the page is : "+self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()