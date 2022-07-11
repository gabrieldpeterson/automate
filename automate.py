from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Safari()

driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
driver.maximize_window()

message_input = driver.find_element(by=By.ID, value='user-message')
message_input.send_keys('test text')

# Don't kill browser immediately after running
while True:
    pass