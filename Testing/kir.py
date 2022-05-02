import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Mystore(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\hp\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()
    def test_sigin(self):
        self.driver.find_element(by=By.XPATH,value="//a[contains(text(),'Sign in')]").click()
        self.driver.find_element(by=By.XPATH,value="//input[@id='email_create']").send_keys("kgk580573@gmail.com")
        self.driver.find_element(by=By.XPATH,value="//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/button[1]/span[1]").click()
        self.driver.find_element(by=By.XPATH,value="//input[@id='id_gender1']").click()
        self.driver.find_element(by=By.XPATH, value="//input[@id='customer_firstname']").send_keys("kiran")
        self.driver.find_element(by=By.XPATH, value="//input[@id='customer_lastname']").send_keys("Gowda K")
        self.driver.find_element(by=By.XPATH, value="//input[@id='passwd']").send_keys("Kiran@580573")
        self.driver.find_element(by=By.XPATH, value="//select[@id='days']").send_keys('13')
        self.driver.find_element(by=By.XPATH, value="//select[@id='months']").send_keys('March')
        self.driver.find_element(by=By.XPATH, value="//select[@id='years']").send_keys('2000')
        self.driver.find_element(by=By.XPATH, value="//input[@id='newsletter']").click()
        self.driver.find_element(by=By.XPATH, value="//input[@id='option']").click()
        self.driver.find_element(by=By.XPATH, value="//input[@id='firstname']").send_keys("")
        self.driver.find_element(by=By.XPATH, value="//input[@id='lastname']").send_keys("")
        self.driver.find_element(by=By.XPATH, value="//input[@id='company']").send_keys("COMPANY")
        self.driver.find_element(by=By.XPATH, value="//input[@id='address1']").send_keys("690 1st main road")
        self.driver.find_element(by=By.XPATH, value="//input[@id='address2']").send_keys(" Capgemini ")
        self.driver.find_element(by=By.XPATH, value="//input[@id='city']").send_keys("Pune")
        self.driver.find_element(by=By.XPATH, value="//select[@id='id_state']").send_keys('Texas')
        self.driver.find_element(by=By.XPATH, value="//input[@id='postcode']").send_keys(" 560078 ")
        self.driver.find_element(by=By.XPATH, value="//select[@id='id_country']").send_keys('United States')
        self.driver.find_element(by=By.XPATH, value="//textarea[@id='other']").send_keys("Straight bandhu left thagoli amel dead end bandh right thago ali yadrug idhe")
        self.driver.find_element(by=By.XPATH, value="//input[@id='phone']").send_keys("9742580573 ")
        self.driver.find_element(by=By.XPATH, value="//input[@id='phone_mobile']").send_keys(" 9742580573 ")
        self.driver.find_element(by=By.XPATH, value="//input[@id='alias']").send_keys(" Sumne address kelkon ba  ")
        self.driver.find_element(by=By.XPATH,value="//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div[4]/button[1]/span[1]").click()

if __name__=="__main__":
    unittest.main()