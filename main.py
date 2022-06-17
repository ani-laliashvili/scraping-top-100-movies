from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')


titles = soup.find_all(name='h3', class_='title')

movie_titles = [title.getText() + '\n' for title in titles]
movie_titles.reverse()

with open('movies.txt', 'w') as file:
    file.writelines(movie_titles)



