
from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
web_page = response.text

#### get the main title
soup = BeautifulSoup(web_page, 'html.parser')
print(soup.title.string)

#### get all the article titles
article_titles = []
titles = soup.find_all('a', class_= 'storylink')
for t in titles:
    x = t.getText()
    article_titles.append(x)


#### get the first article title
title = soup.find('a', class_='storylink')
print(title.getText())

#### get the first article link
link = soup.find('a', class_='storylink')
print(link.get('href'))

##### get all of the links
article_links = []
links = soup.find_all('a', class_='storylink')
for i in links:
    l = i.get('href')
    article_links.append(l)

upvote = soup.find('span', class_='score').getText()
print(upvote)

article_upvotes = [score.getText().split()[0] for score in soup.find_all('span', class_='score')]
print(int(article_upvotes[0].split()[0]))


print(article_titles)
print(article_links)
print(article_upvotes)

###### Find the article name and link that has the highest upvotes
largest_vote = max(article_upvotes)
print(largest_vote)
largest_index = article_upvotes.index(largest_vote)
print(largest_index)
print('Article that has the highest votes is:',
      article_titles[largest_index], article_links[largest_index])