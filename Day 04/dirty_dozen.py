import requests
from bs4 import BeautifulSoup

url = 'https://www.delish.com/food-news/a26872638/dirty-dozen-foods-list-2019/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

dirty_dozen = soup.find('ol', class_='body_ol')
print(dirty_dozen.getText())