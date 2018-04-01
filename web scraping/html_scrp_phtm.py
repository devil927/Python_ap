# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 17:35:15 2018

@author: Tushar
"""
#  importing the library 
from selenium import webdriver

driver=webdriver.PhantomJS(executable_path=r'phantomjs\bin\phantomjs.exe')

driver.get("http://python.org")

html_cont =driver.page_source

print(html_cont)