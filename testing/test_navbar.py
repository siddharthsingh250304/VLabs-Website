# The idea is to go to the (currently implemented) three screens - namely search, download and add question and check if the buttons are working fine.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

gotolinks = ["/search", "/download", "/add"]

gotolink = "http://localhost:3000/login"

# first login
driver = webdriver.Chrome()
driver.get(gotolink)
driver.implicitly_wait(3)

username_field = driver.find_element(By.ID, "login-email")
username_field.send_keys("testuser@test.com")

password_field = driver.find_element(By.ID, "login-password")
password_field.send_keys("testing")
password_field.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

# driver.get("localhost:3000/search")

def test_search_button():
    search_button = driver.find_element(By.ID, "search_button_navbar")
    search_button.click()
    time.sleep(2)
    driver.implicitly_wait(3)
    
    assert gotolinks[0] in driver.current_url

def test_download_button():
    search_button = driver.find_element(By.ID, "downloadlist_button_navbar")
    search_button.click()
    time.sleep(2)
    
    driver.implicitly_wait(3)
    
    assert gotolinks[1] in driver.current_url

def test_add_button():
    search_button = driver.find_element(By.ID, "add_button_navbar")
    search_button.click()
    time.sleep(2)
    
    driver.implicitly_wait(3)
    
    assert gotolinks[2] in driver.current_url
    driver.quit()