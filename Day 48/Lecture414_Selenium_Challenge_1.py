from selenium import webdriver

chrome_driver_path = '/Users/dennie/Development/chromedriver'
driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get('https://www.python.org/')

event_names = driver.find_elements_by_css_selector('.event-widget time')
event_times = driver.find_elements_by_css_selector('.event-widget ul a')
events = {}
for i in range(len(event_names)):
    events[i] = {
        'names':event_names[i].text, 'times':event_times[i].text
    }
print(events)
driver.close()