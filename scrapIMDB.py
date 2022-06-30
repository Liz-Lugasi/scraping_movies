

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
    


    #requesr

    web_site = "https://www.imdb.com/chart/top/"
    response = requests.get(web_site) #200
    html = response.content 
    #soup
    soup = BeautifulSoup(html, 'lxml') #making a soup (,"lxml")
    #print(soup.prettify())
   

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
    genre_list = []
    cast_list = []      
    
    for movie in movies:   
        #more information on each movie page
        print(index,"/",movies_amount)
        
        movie_url = urljoin(web_site, movie.find('td',class_="titleColumn").a['href'])
        response_page = requests.get(movie_url)
        html_page = response_page.content 
        soup_page = BeautifulSoup(html_page, 'lxml') 
             
        genre_links = soup_page.find('div',attrs={'data-testid': 'genres'}).find_all('a')
        genres_cur_list = list_to_string((a['href'].split("="))[1].split("&")[0] for a in genre_links)
        genre_list.append(genres_cur_list)
                
            
        
        try:
            popularity = soup_page.find('div',attrs={'data-testid': 'hero-rating-bar__popularity__score'}).text
        except Exception as e:
            popularity = "NotFound"
        popularity_list.append(popularity)    
        
        cast = soup_page.find_all('a',class_="sc-18baf029-1 gJhRzH")
        cast_list.append(list_to_string([actor.text for actor in cast]))
        
        director_list.append(soup_page.find('a',class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text)
        
        index += 1
     
     
    movies = pd.DataFrame()
    movies["movie name"] = name_list
    movies["year"] = year_list
    movies["rate"] = rate_list
    movies["cast"] = cast_list
    movies["popularity"] = popularity_list
    movies["director"] = director_list
    movies["genres"] = genre_list
    movies["rank"] = rank_list
    movies.head(50)

        
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


def list_to_string(list_):
    string = ', '.join([str(item) for item in list_])
    print(string)
    return string 


  
if __name__ == "__main__":
    
    main()
    #test()