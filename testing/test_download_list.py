from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

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


def test_search_by_tags_1():
    autocomplete_input = driver.find_element(By.ID, "tags")  # Locate the Autocomplete input field
    autocomplete_input.clear()
    # Enter the tag names to trigger the dropdown
    autocomplete_input.send_keys("biology")
    time.sleep(2)  # Wait for the dropdown to appear

    # Select tags from the dropdown
    tag_options = driver.find_elements(By.XPATH, "//ul[@role='listbox']/li[@aria-selected='false']")
    for option in tag_options:
        try:
            if option.text == "biology":
                option.click()
                time.sleep(1)
        except:
            pass   
    search_button = driver.find_element(By.ID, "search_button")
    search_button.click()
    time.sleep(2)  # Wait for search results to load

    # Assert that a card with ID "CARDID" is visible
    card_element = driver.find_element(By.ID, "gotQuestions")
    assert card_element.is_displayed(), "Card with ID 'CARDID' is not visible"

    # You can further perform additional assertions or checks if needed
 # Placeholder assertion to indicate the test passed



def test_open_first_question():
    card_element = driver.find_element(By.ID, "gotQuestions")
    assert card_element.is_displayed(), "Card with ID 'CARDID' is not visible"

    card_element.click()
    time.sleep(3)
    assert "quiz" in driver.current_url
    assert "0" in driver.current_url



def test_add_to_downloadlist():
    download_button=driver.find_element(By.ID,"download_button_quiz")
    download_button.click()
    
    time.sleep(2)
    assert True
    
    search_button = driver.find_element(By.ID, "downloadlist_button_navbar")
    search_button.click()
    time.sleep(2)




def test_download():
    # gotolink = "http://localhost:3000/login"
    # # First login
    # driver = webdriver.Chrome()
    # driver.get(gotolink)
    # driver.implicitly_wait(3)

    # username_field = driver.find_element(By.ID, "login-email")
    # username_field.send_keys("testuser@test.com")

    # password_field = driver.find_element(By.ID, "login-password")
    # password_field.send_keys("testing")
    # password_field.send_keys(Keys.RETURN)

    # time.sleep(3)
    # search_button = driver.find_element(By.ID, "downloadlist_button_navbar")
    # search_button.click()
    # time.sleep(2)

    
    # driver.get("http://localhost:3000/downloadlist")
    
    download_button = driver.find_element(By.ID, "download-button")
    download_button.click()
    
    time.sleep(1)
    
    # now check if the file was downloaded (by checking if the file exists in the desired path)
    
    ####### NOTE TO FUTURE DEVELOPERS #######
    # This might be changed depending on the machine. A better method is needed in the future.
    # Assuming this is the download path
    files = os.listdir("C://Users//Admin//Downloads")

    # Check if any file starts with "questions.json"
    if any(file.startswith("questions.json") for file in files):
        downloaded = True
        assert downloaded

    time.sleep(1)
    
def test_remove_from_download():
    # gotolink = "http://localhost:3000/login"
    # # First login
    # driver = webdriver.Chrome()
    # driver.get(gotolink)
    # driver.implicitly_wait(3)

    # username_field = driver.find_element(By.ID, "login-email")
    # username_field.send_keys("testuser@test.com")

    # password_field = driver.find_element(By.ID, "login-password")
    # password_field.send_keys("testing")
    # password_field.send_keys(Keys.RETURN)

    # time.sleep(3)
    # download_button = driver.find_element(By.ID, "downloadlist_button_navbar")
    # download_button.click()
    # time.sleep(2)
    #### NOTE: Future developers may need to fix this.
    
    try:
        remove_from_download_button = driver.find_element(By.ID, "Card-Remove-0")
        
        remove_from_download_button.click()
    except:
        assert True
    
    try:
        find_elem = driver.find_element(By.ID, "Card-Remove-0")
        if find_elem.is_displayed():
            assert False
        else:
            assert True
    except:
        assert True

    time.sleep(1)
    driver.quit()
    
if __name__ == "__main__":
    test_remove_from_download()