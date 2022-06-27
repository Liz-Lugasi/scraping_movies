

#imports

from csv import excel
from urllib import response
from bs4 import BeautifulSoup
import requests, openpyxl
from urllib.parse import urljoin 

#create aexcel
#excel = openpyxl.Workbook()
#sheet = excel.active
#sheet.title = "top rated movies"
#sheet.append(['rank' , "name" , "year" ,"rate"])



try:

#requesr

    web_site = "https://www.imdb.com/chart/top/"
    response = requests.get(web_site) #200
    html = response.text #or .content

    #soup

    soup = BeautifulSoup(html, 'html.parser') #making a soup (,"lxml")
    #print(soup.prettify())

    #find&findall
    #fing all movies
    movies = soup.find('tbody', class_="lister-list").find_all('tr')
    #print(movies)

    for movie in movies:

        name = movie.find('td',class_="titleColumn").a.text
        #rank = movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
        #year = movie.find('td',class_="titleColumn").find('span').text.strip('()')
        #rate = movie.find('td', class_="ratingColumn imdbRating").strong.text
        


        movie_url = urljoin(web_site, movie.find('td',class_="titleColumn").a['href'])

        esponse_page = requests.get(movie_url) #200
        html_page = esponse_page.text #or .content
        soup_page = BeautifulSoup(html_page, 'html.parser') #making a soup (,"lxml")
        popularity = soup_page.find('div',class_="sc-edc76a2-1 gopMqI").text

        print(f'name: {name}',popularity)

        #add to excel
        #sheet.append([rank , name , year ,rate ])
        print("")

except Exception as e:
    print(e)

#save the excel
#excel.save('IMDB.xlsx')