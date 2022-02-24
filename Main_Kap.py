import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import string
import random
import Page_Kap

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/katherinenewcomb/Desktop/Finadvant/chromedriver")
        self.driver.get("https://ib-test.kapaga.com/en/login")

    def test_search_python(self):
        mainPage = Page_Kap.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "E-mail"
        time.sleep(10)
        mainPage.click_go_button()
        search_result_page = Page_Kap.SearchResultsPage(self.driver)
        assert search_result_page.is_results_found()


    #def test_ValidUsername(self):
        #mainPage2 = page.MainPage(self.driver)
        #assert mainPage2.ValidUsername()
        #mainPage2.find_element_by_id(id) = "pycon"
        #mainPage2.send_keys("tutorial")
        #mainPage2.send_keys(Keys.RETURN)
        #time.sleep(100)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
