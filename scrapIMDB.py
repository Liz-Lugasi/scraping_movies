

#imports

from csv import excel
from urllib import response
from bs4 import BeautifulSoup
import requests, openpyxl

#create aexcel
#excel = openpyxl.Workbook()
#sheet = excel.active
#sheet.title = "top rated movies"
#sheet.append(['rank' , "name" , "year" ,"rate"])



try:

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
        rate = movie.find('td', class_="ratingColumn imdbRating").strong.text
        
        #add to excel
        #sheet.append([rank , name , year ,rate ])


except Exception as e:
    print(e)

#save the excel
#excel.save('IMDB.xlsx')