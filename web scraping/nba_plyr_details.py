#============================  fetching  information  about players of nba

#   importing the library
from selenium import webdriver
from bs4 import BeautifulSoup

# class
class player():
    def __init__(self):
        self.name=""
        self.link=""
        self.Height=""
        self.Born=""
        self.Weight=""
#=====================================================================================
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
def details(player_list):
    #=======================================================================================
    for p in player_list:
        driver1 = webdriver.PhantomJS(executable_path=r'phantomjs\bin\phantomjs.exe')
        url=p.link
        driver1.get(url)
        html_cont1 = driver1.page_source
        soup1=BeautifulSoup(html_cont1,'lxml')
        #==================================================================================
        h = ""
        q1 = soup1.find('p',string='''
      HEIGHT
    ''')
        q2=q1.find_next_sibling('p')
        h=h+q2.text
        p.Height=h
        #==================================================================================
        w= ""
        q1 = soup1.find('p',string='''
      WEIGHT
    ''')
        q2 = q1.find_next_sibling('p')
        w = w + q2.text
        p.Weight=w
        #==========================================
        b=""
        q1 = soup1.find('span', string='BORN')
        q2 = q1.find_next_sibling('span')
        b = b + q2.text
        p.Born=b.strip()
    driver1.quit()
    return player_list
#==============================================================
player_list=details(get_name())
for p in player_list:
    print(p.name)
    print(p.Born)
    print(p.Height)
    print(p.Weight)
    print(p.link)
