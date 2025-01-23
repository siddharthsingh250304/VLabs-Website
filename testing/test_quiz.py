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



def test_search_by_tags_1():
    autocomplete_input = driver.find_element(
        By.ID, "tags"
    )  # Locate the Autocomplete input field
    autocomplete_input.clear()
    # Enter the tag names to trigger the dropdown
    autocomplete_input.send_keys("biology")
    time.sleep(2)  # Wait for the dropdown to appear

    # Select tags from the dropdown
    tag_options = driver.find_elements(
        By.XPATH, "//ul[@role='listbox']/li[@aria-selected='false']"
    )
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


def test_forward_button():
    forward = driver.find_element(By.ID, "fwd")
    forward.click()
    time.sleep(2)
    assert "quiz" in driver.current_url
    assert "1" in driver.current_url


def test_backward_button():
    backward = driver.find_element(By.ID, "bwd")
    backward.click()
    time.sleep(2)
    assert "quiz" in driver.current_url
    assert "0" in driver.current_url


def main():
    # test_no_parameters()
    # test_search_by_tags()
    test_init()
    test_search_by_tags_1()
    test_open_first_question()
    test_forward_button()
    driver.quit()


if __name__ == "__main__":
    main()
