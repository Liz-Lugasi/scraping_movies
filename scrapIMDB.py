

#imports


from csv import excel
from pickletools import string1
import string
from urllib import response
from bs4 import BeautifulSoup
import requests, openpyxl
from urllib.parse import urljoin 
import pandas as pd



def main():
    #create aexcel
    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = "top rated movies"
    sheet.append(['rank' , "name" , "year" ,"rate", "popularity","genres" ,"director", "cast"])


    try:

    #requesr

        web_site = "https://www.imdb.com/chart/top/"
        response = requests.get(web_site) #200
        html = response.content 

        #soup

        soup = BeautifulSoup(html, 'lxml') #making a soup (,"lxml")
        #print(soup.prettify())
        with open('IMDB 250 TOP MOVIES','wb') as file:
            file.write(soup.prettify('utf-8'))



        movies = soup.find('tbody', class_="lister-list").find_all('tr')
        #print(movies)
        movies_amount = len(movies)
        index = 0
        
        
        name_list = [movie.find('td',class_="titleColumn").a.text for movie in movies]
        rank_list = [movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0] for movie in movies]
        year_list = [movie.find('td',class_="titleColumn").find('span').text.strip('()') for movie in movies]
        rate_list = [movie.find('td', class_="ratingColumn imdbRating").strong.text for movie in movies]
        popularity_list = []
        director_list = []        
        
        for movie in movies:   
            #more information on each movie page
            
            name = movie.find('td',class_="titleColumn").a.text 
            rank = movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0] 
            year = movie.find('td',class_="titleColumn").find('span').text.strip('()') 
            rate = movie.find('td', class_="ratingColumn imdbRating").strong.text 
            
            
            movie_url = urljoin(web_site, movie.find('td',class_="titleColumn").a['href'])
            response_page = requests.get(movie_url) #200
            html_page = response_page.text #or .content
            soup_page = BeautifulSoup(html_page, 'html.parser') #making a soup (,"lxml")
            try:
                popularity_list.append(soup_page.find('div',class_="sc-edc76a2-1 gopMqI").text)
                popularity = soup_page.find('div',class_="sc-edc76a2-1 gopMqI").text
            except Exception as e:
                popularity = "NotFound"
                popularity_list.append("NotFound")
            
            genre_links = soup_page.find('div',attrs={'data-testid': 'genres'}).find_all('a')

            genres_list = [(a['href'].split("="))[1].split("&")[0] for a in genre_links]
            genre_string = list_to_string([(a['href'].split("="))[1].split("&")[0] for a in genre_links])
            director = soup_page.find('a',class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text
            director_list.append(soup_page.find('a',class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text)
            cast = soup_page.find_all('a',class_="sc-18baf029-1 gJhRzH")
            
            cast_list = [actor.text for actor in cast]
            cast_string = list_to_string([actor.text for actor in cast])
            
            #add to excel
            sheet.append([rank , name , year ,rate, popularity,genre_string ,director, cast_string])
            index += 1

    except Exception as e:
        raise e
    #save the excel
    excel.save('TOP 250 MOVIES IMDB.xlsx')
        
        
def test():        
        
    web_site = "https://www.imdb.com/chart/top/"
    response = requests.get(web_site)
    html = response.content 
    soup = BeautifulSoup(html, 'lxml')
    movies = soup.find('tbody', class_="lister-list").find_all('tr')
    genre_list = []
    for movie in movies:  
      movie_url = urljoin(web_site, movie.find('td',class_="titleColumn").a['href'])
      response_page = requests.get(movie_url)
      html_page = response_page.content 
      soup_page = BeautifulSoup(html_page, 'lxml') 

      genre_links = soup_page.find('div',attrs={'data-testid': 'genres'}).find_all('a')
      genres_cur_list = [(a['href'].split("="))[1].split("&")[0] for a in genre_links]
      genre_list.append(genres_cur_list)
      print(genres_cur_list)  
        
    print(genre_list)


def list_to_string(list_):
    string = ', '.join([str(item) for item in list_])
    print(string)
    return string 


  
if __name__ == "__main__":
    #main()
    test()