
# ======================== Import library
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests
#=================== class
class list:
    def __init__(self):
        self.poster=""
        self.name=""
        self.rating=""
#================================= driver
driver=webdriver.PhantomJS(executable_path=r'phantomjs\bin\phantomjs.exe')
driver.get('http://www.imdb.com/chart/top?sort=ir,desc&mode=simple&page=1')
#================================ fetching the code
html_cont=driver.page_source
soup=BeautifulSoup(html_cont,'lxml')
movie_list=[]
#======================== processing on data
for tr in soup.find_all('tr'):
    m=list()
    poster=tr.find('td',class_='posterColumn')
    name = tr.find('td', class_='titleColumn')
    rating = tr.find('td', class_='ratingColumn imdbRating')
    if name!=None or rating!=None or poster!=None:
        m.poster='https://www.imdb.com'+poster.a['href']
        m.name=name.a.text
        m.rating=rating.text
        movie_list.append(m)
#======================== Movies list
def movies_list(movie_list):
    for list in movie_list:
        print(list.name)
#========================= To store posters of movies
def movie_poster(movie_list):
    for list in movie_list:
        #=========================== To check the folder
        if not os.path.exists('imdb_movie_poster'):
            os.makedirs('imdb_movie_poster')
        #=================================== Driver
        driver1 = webdriver.PhantomJS(executable_path=r'phantomjs\bin\phantomjs.exe')
        driver1.get(list.poster)
        #===================  Html page
        html_cont1 = driver1.page_source
        soup1 = BeautifulSoup(html_cont1, 'lxml')
        p = soup1.find('div')
        k=p.find('div', class_='poster')
        #=============================
        pos_link ='https://www.imdb.com'+ k.a['href']
        driver1.get(pos_link)
        html_cont2=driver1.page_source
        soup1 = BeautifulSoup(html_cont2, 'lxml')
        #================== fetching the image details
        p = soup1.find('img')
        k=p['src']
        f=open('imdb_movie_poster/{0}.jpg'.format(list.name),'wb')
        f.write(requests.get(k).content)
        f.close()
        driver1.quit()
        driver.quit()
#=============================================================
movie_poster(movie_list)
movies_list(movie_list)
