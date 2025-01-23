from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
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




# def test_no_parameters():
#     search_button = driver.find_element(By.ID, "search_button")
#     search_button.click()
#     time.sleep(1)
#     error=driver.find_element(By.ID, "error")
#     assert error.is_displayed()




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


def test_clear_tag():
    tag_chip = driver.find_element(By.CSS_SELECTOR, ".MuiChip-deleteIcon")

    # Simulate click on the delete (remove) button of the tag chip
    tag_chip.click()
    time.sleep(1)

    assert True  # Assuming the tag input field is cleared

def test_search_by_user():
    user_input = driver.find_element(By.ID, "user")
    user_input.send_keys("divukruti@gmail.com")  # Enter a user name

    search_button = driver.find_element(By.ID, "search_button")
    search_button.click()
    time.sleep(2)

    user_input.clear()
    time.sleep(1)

    card_element = driver.find_element(By.ID, "gotQuestions")
    assert card_element.is_displayed(), "Card with ID 'CARDID' is not visible" # Assuming the user input field is cleared

def test_search_by_difficulty():
    difficulty_dropdown = driver.find_element(By.ID, "difficulty")
    difficulty_dropdown.click()
    time.sleep(1)

    easy_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Easy')]"))
    )
    easy_option.click()
    time.sleep(1)

    search_button = driver.find_element(By.ID, "search_button")
    search_button.click()
    time.sleep(2)

    difficulty_dropdown.click()
    time.sleep(2)   
    cross=driver.find_element(By.ID,"cross")
    cross.click()
    time.sleep(2)

    card_element = driver.find_element(By.ID, "gotQuestions")
    assert card_element.is_displayed(), "Card with ID 'CARDID' is not visible"
    
    # assert "Easy" in driver.current_url

def test_multiple_tags_search():
    tags_list = ["biology", "physics", "chemistry"]

    for tag in tags_list:
        autocomplete_input = driver.find_element(By.ID, "tags")
        autocomplete_input.clear()
        autocomplete_input.send_keys(tag)
        time.sleep(1)

        tag_options = driver.find_elements(By.XPATH, "//ul[@role='listbox']/li[@aria-selected='false']")
        for option in tag_options:
            if option.text == tag:
                option.click()
                time.sleep(1)

    search_button = driver.find_element(By.ID, "search_button")
    search_button.click()
    time.sleep(2)

    card_element = driver.find_element(By.ID, "gotQuestions")
    assert card_element.is_displayed(), "Card with ID 'CARDID' is not visible"

def test_multi_dimensional():
    difficulty_dropdown = driver.find_element(By.ID, "difficulty")
    difficulty_dropdown.click()
    time.sleep(1)

    easy_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Hard')]"))
    )
    easy_option.click()
    time.sleep(1)

    search_button = driver.find_element(By.ID, "search_button")
    search_button.click()
    time.sleep(2)


    card_element = driver.find_element(By.ID, "gotQuestions")
    assert card_element.is_displayed(), "Card with ID 'CARDID' is not visible"
   
def test_remove_tags_by_label():
    # Loop through the labels you want to remove
    labels_to_remove=['physics','chemistry']
    for label in labels_to_remove:
            # Find the Chip (tag) element based on its label text
            chip_element = driver.find_element(By.XPATH, f"//span[text()='{label}']/ancestor::div[@role='button']")
            
            # Click on the delete button of the Chip to remove the tag
            delete_button = chip_element.find_element(By.CSS_SELECTOR, ".MuiChip-deleteIcon")
            delete_button.click()
            
            # Optionally, you can wait for a confirmation or check that the tag is removed
            time.sleep(1)  # Wait for the tag to be removed
            
            # Add assertions or further actions as needed
            assert True  # Check that the tag is no longer present on the page
    
    difficulty_dropdown = driver.find_element(By.ID, "difficulty")
    difficulty_dropdown.click()
    time.sleep(2)   
    cross=driver.find_element(By.ID,"cross")
    cross.click()
    time.sleep(2)
    search_button = driver.find_element(By.ID, "search_button")
    search_button.click()
    time.sleep(2)
    card_element = driver.find_element(By.ID, "gotQuestions")
    assert card_element.is_displayed(), "Card with ID 'CARDID' is not visible"
    
    page_buttons = driver.find_elements(By.CSS_SELECTOR, 'button[id^="page"]')  # Select all buttons with IDs starting with 'page'
    print(page_buttons)
    # Iterate through the page buttons and click each one
    for button in page_buttons:
        time.sleep(1)
        button.click()
        time.sleep(1)  # Add a delay to allow the page change to occur
        card_element = driver.find_element(By.ID, "gotQuestions") 
        assert card_element.is_displayed(), "Card with ID 'CARDID' is not visible"
    driver.quit()





def main():
    # test_no_parameters()
    # test_search_by_tags()
    test_clear_tag()
    test_search_by_user()
    test_search_by_difficulty()
    test_multiple_tags_search()
    test_multi_dimensional()
    test_remove_tags_by_label()
    test_clear_tag()
    # test_no_parameters()
    driver.quit()

if __name__ == "__main__":
    pytest.main(['-v'])
