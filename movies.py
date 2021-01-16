from bs4 import BeautifulSoup
import requests

url = 'https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(url)
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
print(soup.title)

all_movies = soup.find_all('h3', class_='title')

"""titles = []
for t in title:
    x = t.getText()
    titles.append(x)
print(titles[::-1])

"""
movie_titles = [movie.getText() for movie in all_movies]
movie = movie_titles[::-1]

with open('电影.txt', mode='w') as file:
    for i in movie:
        file.write(f'{i}\n')

