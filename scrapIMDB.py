

#imports

from urllib import response
from bs4 import BeautifulSoup
import requests

#requesr

web_site = "https://www.imdb.com/chart/top/"
response = requests.get(web_site)
html = response.text

#soup

soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())

#find&findall
#fing all movies
movies = soup.find('tbody', class_="lister-list").find_all('tr')
#print(movies)

for movie in movies:

    name = movie.find('td',class_="titleColumn").a.text
    rank = movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
    year = movie.find('td',class_="titleColumn").find('span').text.strip('()')
    rate = movie.find('td', class_="ratingColumn imdbRating").text
    print('rank: ' ,rank, "name: " ,name, "year: " , year ,"rate: ",rate)



