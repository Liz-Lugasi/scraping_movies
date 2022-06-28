

#imports


from csv import excel
from urllib import response
from bs4 import BeautifulSoup
import requests, openpyxl
from urllib.parse import urljoin 


def main():
    #create aexcel
    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = "top rated movies"
    sheet.append(['rank' , "name" , "year" ,"rate", "popularity","genres_list" ,"director"])


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
        for movie in movies:
            print(index,'/',movies_amount)
            name = movie.find('td',class_="titleColumn").a.text
            rank = movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
            year = movie.find('td',class_="titleColumn").find('span').text.strip('()')
            rate = movie.find('td', class_="ratingColumn imdbRating").strong.text
            
            #more information on each movie page
            movie_url = urljoin(web_site, movie.find('td',class_="titleColumn").a['href'])
            response_page = requests.get(movie_url) #200
            html_page = response_page.text #or .content
            soup_page = BeautifulSoup(html_page, 'html.parser') #making a soup (,"lxml")
            try:
                popularity = soup_page.find('div',class_="sc-edc76a2-1 gopMqI").text
            except Exception as e:
                popularity = "NotFound"
            
            genre_links = soup_page.find('div',class_="ipc-chip-list sc-16ede01-4 bMBIRz").find_all('a')
            genres_list = [(a['href'].split("="))[1].split("&")[0] for a in genre_links]
            director = soup_page.find('a',class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text
            
            #add to excel
            sheet.append([rank , name , year ,rate, popularity,genres_list ,director])
            index += 1

    except Exception as e:
        print(e)

    #save the excel
    excel.save('IMDB.xlsx')

def test():
    movie_url = "https://www.imdb.com/title/tt0027977/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=DTTD15ND3MZA3P0PNY1J&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_46"
    esponse_page = requests.get(movie_url) #200
    html_page = esponse_page.text #or .content
    soup_page = BeautifulSoup(html_page, 'html.parser') #making a soup (,"lxml")
    try:
        popularity = soup_page.find('div',class_="sc-edc76a2-1 gopMqI").text
    except Exception as e:
        popularity = "NotFound"





def test2():
    web_site = "https://www.imdb.com/chart/top/"
    response = requests.get(web_site) #200
    html = response.content 
    #soup
    soup = BeautifulSoup(html, 'lxml') #making a soup (,"lxml")
    #print(soup.prettify())
    with open('IMDB 250 TOP MOVIES','wb') as file:
        file.write(soup.prettify('utf-8'))
        
        
def test3():        
        
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
    for movie in movies:
        print(index,'/',movies_amount)
        name = movie.find('td',class_="titleColumn").a.text
        
        movie_url = urljoin(web_site, movie.find('td',class_="titleColumn").a['href'])
        esponse_page = requests.get(movie_url) #200
        html_page = esponse_page.text #or .content
        soup_page = BeautifulSoup(html_page, 'html.parser') #making a soup (,"lxml")

        #cast = soup_page.find('a',class_="sc-18baf029-1 gJhRzH").text  #work for the first
            
        cast = soup_page.find_all('a',class_="sc-18baf029-1 gJhRzH")
        cast_list = [a.text for a in cast]

        #cast_list = [cast.text for a in cast]

        
        
        print(name,cast_list)
        index += 1
        
if __name__ == "__main__":
    #main()
    test3()