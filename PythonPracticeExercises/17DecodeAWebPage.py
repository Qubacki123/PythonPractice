# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:24:26 2019

@author: kubac
"""

import requests
from bs4 import BeautifulSoup

def zapytanie():
    adres = 'https://www.nytimes.com/'
    odpowiedz = requests.get(adres)
    nyt_html = odpowiedz.text
    return nyt_html

soup = BeautifulSoup(zapytanie(),"lxml")

i=1
for naglowek in soup.find_all('h2'):
    print("%d. "% i + str(naglowek.contents[0]))
    i = i + 1
    print('----------')



    