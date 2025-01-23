from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import string
import random


driver = webdriver.Chrome()


website_url = "http://localhost:3000/login"
driver.get(website_url)

driver.implicitly_wait(3)

username_field = driver.find_element(By.ID, "login-email")
username_field.send_keys("testuser@test.com")

password_field = driver.find_element(By.ID, "login-password")
password_field.send_keys("testing")
password_field.send_keys(Keys.RETURN)
time.sleep(5)

# driver.get("localhost:3000/search")


def test_profile_button():
    mini_bar=driver.find_element(By.ID,"mini_bar")
    mini_bar.click()
    time.sleep(2)
    
    profile_button=driver.find_element(By.ID,"profile_option")
    profile_button.click()
    time.sleep(3)
    
    assert "profile" in driver.current_url


def test_API_docs():
    mini_bar=driver.find_element(By.ID,"mini_bar")
    mini_bar.click()
    time.sleep(2)
    
    api_button=driver.find_element(By.ID,"api_button")
    api_button.click()
    time.sleep(3)
    
    assert "api_documentation" in driver.current_url

def test_logout():
    mini_bar=driver.find_element(By.ID,"mini_bar")
    mini_bar.click()
    time.sleep(2)
    
    logout=driver.find_element(By.ID,"logout")
    logout.click()
    time.sleep(3)
    
    assert "login" in driver.current_url
    driver.quit()



def main():
    # test_no_parameters()
    # test_search_by_tags()
    test_profile_button()
    test_API_docs()
    test_logout()
    driver.quit()


if __name__ == "__main__":
    main()

















