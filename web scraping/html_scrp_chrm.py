# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 17:35:15 2018

@author: Tushar
"""
#  importing the library 
from selenium import webdriver

driver=webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("http://www.facebook.com")

html_cont =driver.page_source

from bs4 import BeautifulSoup

soup=BeautifulSoup(html_cont,'lxml')

print(soup.prettify())
