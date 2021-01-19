from selenium import webdriver

chrome_driver_path = '/Users/dennie/Development/chromedriver'
driver = webdriver.Chrome(executable_path = chrome_driver_path)

'''
#### close a particular tab
#driver.close()
#### close the entire browser
#driver.quit()
'''

driver.get('https://www.python.org/')
#price = driver.find_element_by_id('priceblock_ourprice')
#print(price.text)

#search_bar = driver.find_element_by_name('q')
#print(search_bar.get_attribute('placeholder'))

#logo = driver.find_element_by_class_name('python-logo')
#print(logo.size)

#documentation_link = driver.find_element_by_css_selector('.documentation-widget a')
#print(documentation_link.text)

bug_link = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[1]/div[4]/p[2]/a')
print(bug_link.text)
driver.close()