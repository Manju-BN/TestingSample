import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Registration(unittest.TestCase):

    def setUp(self):
        global driver
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\hp\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()

    def test_Signin(self):

        self.driver.find_element(by=By.XPATH,value="//a[contains(text(),'Sign in')]").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value="//input[@id='email_create']").send_keys("rockyceo14@gmail.com")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value="//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/button[1]/span[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//input[@id='id_gender1']").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//input[@id='customer_firstname']").send_keys("Rocky")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//input[@id='customer_lastname']").send_keys("CEO")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//input[@id='passwd']").send_keys("rocky#14")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//select[@id='days']").send_keys(5)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//select[@id='months']").send_keys("May")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//select[@id='years']").send_keys(2000)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//input[@id='newsletter']").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//input[@id='company']").send_keys("Hombale")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//input[@id='address1']").send_keys("#1st cross,2nd main,Church road,Hombale")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//input[@id='address2']").send_keys("#14,Narachi,KGF")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//input[@id='city']").send_keys("Austin")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value="//select[@id='id_state']").send_keys("Alaska")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//input[@id='postcode']").send_keys(10292)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//textarea[@id='other']").send_keys("Go straight and take U turn")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//input[@id='phone']").send_keys(5671211)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//input[@id='phone_mobile']").send_keys(9845607146)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//input[@id='alias']").send_keys("Rocky@KGF")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div[4]/button[1]/span[1]").click()
        time.sleep(5)

        def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__=="__main__":
    unittest.main()





