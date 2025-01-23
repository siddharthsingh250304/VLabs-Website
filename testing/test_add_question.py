from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import string
import random

# Sweat after successfully completing this :_)
def test_successful_question_submission():
    gotolink = "http://localhost:3000/login"

    # First login
    driver = webdriver.Chrome()
    driver.get(gotolink)
    driver.implicitly_wait(3)

    username_field = driver.find_element(By.ID, "login-email")
    username_field.send_keys("testuser@test.com")

    password_field = driver.find_element(By.ID, "login-password")
    password_field.send_keys("testing")
    password_field.send_keys(Keys.RETURN)

    time.sleep(3)
    driver.get("http://localhost:3000/add")
    time.sleep(1)

    # Question
    question_input_box = driver.find_element(By.ID, "Question")
    question_input_box.send_keys("What is the powerhouse of a cell")

    # Options
    NUM_OPTIONS = 4
    options = ["A", "B", "C", "D"]

    for i in range(NUM_OPTIONS):
        current_option = options[i]
        option_input_box = driver.find_element(By.ID, f"Option-{current_option}")

        # Generating random text for each option
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        option_input_box.send_keys(f"Option {current_option} - {random_text}")

        option_explanation_input_box = driver.find_element(By.ID, f"Explanation-{current_option}")
        
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        option_explanation_input_box.send_keys(f"Option {current_option} Explanation - {random_text}")
        
        
    ################## CORRECT OPTION ##################
    autocomplete_input = driver.find_element(By.ID, "select-correct-option")  # Locate the Autocomplete input field

    autocomplete_input.send_keys("Option A")
    time.sleep(1)

    tag_options = driver.find_elements(By.XPATH, "//ul[@role='listbox']/li[@aria-selected='false']")
    for option in tag_options:
        try:
            if option.text == "Option A":
                option.click()
                time.sleep(1)
        except:
            pass
            
            
    ################## DIFFICULTY ##################
    autocomplete_input = driver.find_element(By.ID, "select-difficulty")  # Locate the Autocomplete input field
    autocomplete_input.click()

    easy_difficulty = driver.find_element(By.ID, "easy-difficulty")  # Locate the Autocomplete input field
    easy_difficulty.click()

    # autocomplete_input.send_keys("easy")
    # time.sleep(1)

    # tag_options = driver.find_elements(By.XPATH, "//ul[@role='listbox']/li[@aria-selected='false']")
    # time.sleep(1)
    # for option in tag_options:
    #     try:
    #         if option.text == "easy":
    #             option.click()
    #             time.sleep(1)
    #     except:
    #         pass    
        
        
    ################## TAGS ##################
    autocomplete_input = driver.find_element(By.ID, "tags-outlined-0")  # Locate the Autocomplete input field
    autocomplete_input.send_keys("physics")
    time.sleep(1)

    tag_options = driver.find_elements(By.XPATH, "//ul[@role='listbox']/li[@aria-selected='false']")
    for option in tag_options:
        try:
            if option.text == "physics":
                option.click()
                time.sleep(1)
        except:
            pass
        
    time.sleep(1)

    add_tag_button = driver.find_element(By.ID, "add-tag-button")

    add_tag_button.click()

    submit_button = driver.find_element(By.ID, "submit-button")

    submit_button.click()

    time.sleep(2)

    ########## NOTE FOR FUTURE DEVELOPERS ON THIS PROJECT ##########
    # An alert only appears when a question is submitted successfully. For now this can be used as a testing method. Future developers who might want to extend this, might have to change the following mechanism for checking if the question was submitted successfully through frontend means.
    try:
        alert = driver.switch_to.alert
        alert.accept()
        assert True
    except:
        assert False

    driver.quit()
    
    
def test_omitted_correct_option_question_submission():
    gotolink = "http://localhost:3000/login"

    # First login
    driver = webdriver.Chrome()
    driver.get(gotolink)
    driver.implicitly_wait(3)

    username_field = driver.find_element(By.ID, "login-email")
    username_field.send_keys("testuser@test.com")

    password_field = driver.find_element(By.ID, "login-password")
    password_field.send_keys("testing")
    password_field.send_keys(Keys.RETURN)

    time.sleep(3)
    driver.get("http://localhost:3000/add")
    time.sleep(1)

    # Question
    question_input_box = driver.find_element(By.ID, "Question")
    question_input_box.send_keys("What is the powerhouse of a cell")

    # Options
    NUM_OPTIONS = 4
    options = ["A", "B", "C", "D"]

    for i in range(NUM_OPTIONS):
        current_option = options[i]
        option_input_box = driver.find_element(By.ID, f"Option-{current_option}")

        # Generating random text for each option
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        option_input_box.send_keys(f"Option {current_option} - {random_text}")

        option_explanation_input_box = driver.find_element(By.ID, f"Explanation-{current_option}")
        
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        option_explanation_input_box.send_keys(f"Option {current_option} Explanation - {random_text}")
        
        
    ################## (OMIT) CORRECT OPTION ##################
    if False:
        autocomplete_input = driver.find_element(By.ID, "select-correct-option")  # Locate the Autocomplete input field

        autocomplete_input.send_keys("Option A")
        time.sleep(1)

        tag_options = driver.find_elements(By.XPATH, "//ul[@role='listbox']/li[@aria-selected='false']")
        for option in tag_options:
            try:
                if option.text == "Option A":
                    option.click()
                    time.sleep(1)
            except:
                pass
            
            
    ################## DIFFICULTY ##################
    autocomplete_input = driver.find_element(By.ID, "select-difficulty")  # Locate the Autocomplete input field
    autocomplete_input.click()

    easy_difficulty = driver.find_element(By.ID, "easy-difficulty")  # Locate the Autocomplete input field
    easy_difficulty.click()

    # autocomplete_input.send_keys("easy")
    # time.sleep(1)

    # tag_options = driver.find_elements(By.XPATH, "//ul[@role='listbox']/li[@aria-selected='false']")
    # time.sleep(1)
    # for option in tag_options:
    #     try:
    #         if option.text == "easy":
    #             option.click()
    #             time.sleep(1)
    #     except:
    #         pass    
        
        
    ################## TAGS ##################
    autocomplete_input = driver.find_element(By.ID, "tags-outlined-0")  # Locate the Autocomplete input field
    autocomplete_input.send_keys("physics")
    time.sleep(1)

    tag_options = driver.find_elements(By.XPATH, "//ul[@role='listbox']/li[@aria-selected='false']")
    for option in tag_options:
        try:
            if option.text == "physics":
                option.click()
                time.sleep(1)
        except:
            pass
        
    time.sleep(1)

    add_tag_button = driver.find_element(By.ID, "add-tag-button")

    add_tag_button.click()

    submit_button = driver.find_element(By.ID, "submit-button")

    submit_button.click()

    time.sleep(2)

    ########## NOTE FOR FUTURE DEVELOPERS ON THIS PROJECT ##########
    # An alert only appears when a question is submitted successfully. For now this can be used as a testing method. Future developers who might want to extend this, might have to change the following mechanism for checking if the question was submitted successfully through frontend means.
    try:
        alert = driver.switch_to.alert
        alert.accept()
        assert False
    except:
        assert True

    driver.quit()

    
def test_omitted_option_and_explanation_question_submission():
    gotolink = "http://localhost:3000/login"

    # First login
    driver = webdriver.Chrome()
    driver.get(gotolink)
    driver.implicitly_wait(3)

    username_field = driver.find_element(By.ID, "login-email")
    username_field.send_keys("testuser@test.com")

    password_field = driver.find_element(By.ID, "login-password")
    password_field.send_keys("testing")
    password_field.send_keys(Keys.RETURN)

    time.sleep(3)
    driver.get("http://localhost:3000/add")
    time.sleep(1)

    # Question
    question_input_box = driver.find_element(By.ID, "Question")
    question_input_box.send_keys("What is the powerhouse of a cell")

    # Options
    NUM_OPTIONS = 4
    options = ["A", "B", "C", "D"]

    for i in range(NUM_OPTIONS):
        #### Omitting one option
        if i == 2:
            continue
        current_option = options[i]
        option_input_box = driver.find_element(By.ID, f"Option-{current_option}")

        # Generating random text for each option
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        option_input_box.send_keys(f"Option {current_option} - {random_text}")

        option_explanation_input_box = driver.find_element(By.ID, f"Explanation-{current_option}")
        
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        option_explanation_input_box.send_keys(f"Option {current_option} Explanation - {random_text}")
        
        
    ################## CORRECT OPTION ##################
    autocomplete_input = driver.find_element(By.ID, "select-correct-option")  # Locate the Autocomplete input field

    autocomplete_input.send_keys("Option A")
    time.sleep(1)

    tag_options = driver.find_elements(By.XPATH, "//ul[@role='listbox']/li[@aria-selected='false']")
    for option in tag_options:
        try:
            if option.text == "Option A":
                option.click()
                time.sleep(1)
        except:
            pass
            
            
    ################## DIFFICULTY ##################
    autocomplete_input = driver.find_element(By.ID, "select-difficulty")  # Locate the Autocomplete input field
    autocomplete_input.click()

    easy_difficulty = driver.find_element(By.ID, "easy-difficulty")  # Locate the Autocomplete input field
    easy_difficulty.click()

    # autocomplete_input.send_keys("easy")
    # time.sleep(1)

    # tag_options = driver.find_elements(By.XPATH, "//ul[@role='listbox']/li[@aria-selected='false']")
    # time.sleep(1)
    # for option in tag_options:
    #     try:
    #         if option.text == "easy":
    #             option.click()
    #             time.sleep(1)
    #     except:
    #         pass    
        
        
    ################## TAGS ##################
    autocomplete_input = driver.find_element(By.ID, "tags-outlined-0")  # Locate the Autocomplete input field
    autocomplete_input.send_keys("physics")
    time.sleep(1)

    tag_options = driver.find_elements(By.XPATH, "//ul[@role='listbox']/li[@aria-selected='false']")
    for option in tag_options:
        try:
            if option.text == "physics":
                option.click()
                time.sleep(1)
        except:
            pass
        
    time.sleep(1)

    add_tag_button = driver.find_element(By.ID, "add-tag-button")

    add_tag_button.click()

    submit_button = driver.find_element(By.ID, "submit-button")

    submit_button.click()

    time.sleep(2)

    ########## NOTE FOR FUTURE DEVELOPERS ON THIS PROJECT ##########
    # An alert only appears when a question is submitted successfully. For now this can be used as a testing method. Future developers who might want to extend this, might have to change the following mechanism for checking if the question was submitted successfully through frontend means.
    try:
        alert = driver.switch_to.alert
        alert.accept()
        assert False
    except:
        assert True

    driver.quit()


if __name__ == "__main__":
    test_successful_question_submission()
    test_omitted_correct_option_question_submission()
    test_omitted_option_and_explanation_question_submission()