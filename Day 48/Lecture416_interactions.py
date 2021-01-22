from selenium import webdriver
from selenium.webdriver.common.keys import Keys #implement keys on keyboard

chrome_driver_path = '/Users/dennie/Development/chromedriver'
driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

'''Find the article count number and click on it'''
article_count = driver.find_element_by_css_selector('#articlecount a')
#article_count.click()

'''Find the word History and click on it'''
hist = driver.find_element_by_link_text('History')
#hist.click()

'''Type Python in the search bar'''
search = driver.find_element_by_name('search')
search.send_keys('Python')
search.send_keys(Keys.ENTER) #implement the ENTER key on keyboard