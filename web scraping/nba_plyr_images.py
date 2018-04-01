#============================  fetching images of players of nba

#   importing the library
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests

# class
class player():
    def __init__(self):
        self.name=""
        self.link=""
def get_name():
    #==================================================================== calling driver
    driver = webdriver.PhantomJS(executable_path=r'phantomjs\bin\phantomjs.exe')
    driver.get("http://www.nba.com/players")
    #============================================== geting the html code
    html_cont = driver.page_source
    player_list = []
    #===========================================  parsing the code
    soup = BeautifulSoup(html_cont, 'html.parser')
    #============================================ finding the div for player list
    f = soup.find('div', {'id': 'player-list'})
    #=========================== fetching the information of players
    for a in f.find_all('a', href=True):
        new_player = player()
        new_player.name = a['title']
        new_player.link = "http://www.nba.com"+a['href']
        player_list.append(new_player)
    driver.quit()
    return player_list
#=========================================================================================
def pics(player_list):
    #=====================================================================================
    if not os.path.exists('nba_player'):
        os.makedirs('nba_player')
    #=====================================================================================
    for p in player_list:
        driver1 = webdriver.PhantomJS(executable_path=r'phantomjs\bin\phantomjs.exe')
        url=p.link
        driver1.get(url)
        html_cont1 = driver1.page_source
        #=================================================================== importing the source file
        soup1=BeautifulSoup(html_cont1,'lxml')
        f=soup1.find('player-detail')
        i=f.find('img')
        s=i['src']
        #==================================================================== make an file and upload
        f=open('nba_player\{0}.jpg'.format(p.name),'wb')
        f.write(requests.get(s).content)
        f.close()
#=========================================================================================
pics(get_name())