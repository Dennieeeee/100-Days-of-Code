from selenium import webdriver
from selenium.webdriver.common.keys import Keys #implement keys on keyboard

chrome_driver_path = '/Users/dennie/Development/chromedriver'
driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element_by_name('fName')
first_name.send_keys('aaa')
last_name = driver.find_element_by_name('lName')
last_name.send_keys('bbb')
email = driver.find_element_by_name('email')
email.send_keys('aaabbb@gmail.com')

signup = driver.find_element_by_css_selector('form button')
#<button class="btn btn-lg btn-primary btn-block" type="submit">Sign Up</button>
signup.click()
