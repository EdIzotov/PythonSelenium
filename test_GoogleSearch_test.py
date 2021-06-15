from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("D:/Soft/WebDriversSelenium/chromedriver.exe")

    def testSearch(self):
        driver = self.driver
        search = "ferrari"
        driver.get("https://www.google.com.ua/")
        driver.find_element_by_name("q").send_keys(search)
        driver.find_element_by_name("q").send_keys(Keys.ENTER)

        elements = driver.find_elements_by_css_selector("div.g")
        for el in elements:
            assert search in str(el.text).lower()

    def tearDown(self):
        driver = self.driver
        driver.quit()
