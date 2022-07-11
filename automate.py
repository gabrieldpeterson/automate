from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Safari()

driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
driver.maximize_window()

message_input = driver.find_element(by=By.ID, value='user-message')
message_input.clear()
message_input.send_keys('test text')

message_button = driver.find_element(by=By.XPATH, value='//button[normalize-space()="Show Message"]')
message_button.click()

output_message = driver.find_element(by=By.ID, value='display')

assert 'test text' in output_message.text

# Don't kill browser immediately after running
while True:
    pass
