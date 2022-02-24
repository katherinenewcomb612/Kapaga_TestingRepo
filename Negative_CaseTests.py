from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import string
import random

PATH = "/Users/katherinenewcomb/Desktop/Finadvant/chromedriver"
driver = webdriver.Chrome(PATH)

def get_WebTitle(URL):
    driver.get(URL)
    print(driver.title)

#Negative Test: Only username input
def ValidUsername(id,username):
    type = driver.find_element_by_id(id)
    type.send_keys(username)
    type.send_keys(Keys.RETURN)
    time.sleep(5)

#Negative Test: No inputs
def No_Inputs(id,username):
    type = driver.find_element_by_id(id)
    type.send_keys(username)
    type.send_keys(Keys.RETURN)
    time.sleep(5)

#Negative Test: Password only input
def ValidPassword(id, username):
    type = driver.find_element_by_id(id)
    type.send_keys(username)
    type.send_keys(Keys.RETURN)
    time.sleep(5)

#Negative Test: Invalid username input
def InvalidUsername(id):
    type = driver.find_element_by_id(id)
    type.send_keys(string.ascii_letters)
    type.send_keys(Keys.RETURN)
    time.sleep(5)


get_WebTitle("https://ib-test.kapaga.com/en/login")
#ValidUsername("ClientLoginFormLogin","FN00000ZN")
#No_Inputs("ClientLoginFormLogin","")
ValidPassword("ClientLoginFormPassword","111111")
#InvalidUsername("ClientLoginFormLogin")

driver.quit()
