from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import string
import random

website_url = "http://localhost:3000/login"

def test_login():
    target_url = "search"
    
    driver = webdriver.Chrome()

    driver.get(website_url)
    
    driver.implicitly_wait(3)
    
    username_field = driver.find_element(By.ID, "login-email")
    username_field.send_keys("testuser@test.com")
    
    password_field = driver.find_element(By.ID, "login-password")
    password_field.send_keys("testing")
    
    password_field.send_keys(Keys.RETURN)
 
    time.sleep(5)
 
    assert target_url in driver.current_url
 
    driver.quit()
    
def test_successful_signup():
    target_url = "search"
    
    driver = webdriver.Chrome()

    driver.get(website_url)
    
    driver.implicitly_wait(3)
    
    sign_up_button = driver.find_element(By.ID, "toggle_login_signup")
    
    sign_up_button.click()
    
    username_field = driver.find_element(By.ID, "login-email")
    
    demo_email = f"{''.join(random.choices(string.ascii_uppercase + string.digits, k=7))}@signuptest.com"
    
    username_field.send_keys(demo_email)
    
    password_field = driver.find_element(By.ID, "login-password")
    password_field.send_keys("testing")
    
    password_field.send_keys(Keys.RETURN)
 
    time.sleep(5)
 
    assert target_url in driver.current_url
 
    driver.quit()
    
def test_email_already_taken_signup():
    target_url = "search"
    
    driver = webdriver.Chrome()

    driver.get(website_url)
    
    driver.implicitly_wait(3)
    
    sign_up_button = driver.find_element(By.ID, "toggle_login_signup")
    
    sign_up_button.click()
    
    username_field = driver.find_element(By.ID, "login-email")
    
    already_taken_email = "alreadytakenemail@signuptest.com"
    
    username_field.send_keys(already_taken_email)
    
    password_field = driver.find_element(By.ID, "login-password")
    password_field.send_keys("testing")
    
    password_field.send_keys(Keys.RETURN)
 
    time.sleep(5)
 
    error_box_login_signup = driver.find_element(By.ID, "error_box_login_signup")
 
    assert "error/200" in error_box_login_signup.text
 
    driver.quit()
    
    
    
if __name__ == "__main__":
    test_email_already_taken_signup()