

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
    sheet.append(['rank' , "name" , "year" ,"rate", "popularity"])


    try:

    #requesr

        web_site = "https://www.imdb.com/chart/top/"
        response = requests.get(web_site) #200
        html = response.content 

        #soup

        soup = BeautifulSoup(html, 'html.parser') #making a soup (,"lxml")
        #print(soup.prettify())

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
            
            movie_url = urljoin(web_site, movie.find('td',class_="titleColumn").a['href'])
            esponse_page = requests.get(movie_url) #200
            html_page = esponse_page.text #or .content
            soup_page = BeautifulSoup(html_page, 'html.parser') #making a soup (,"lxml")
            try:
                popularity = soup_page.find('div',class_="sc-edc76a2-1 gopMqI").text
            except Exception as e:
                popularity = "NotFound"
            #add to excel
            sheet.append([rank , name , year ,rate, popularity ])
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

if __name__ == "__main__":
    main()
    #test()