# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 22:18:48 2019

@author: kubac
"""

import random

a = str(random.randint(1,9))

liczba = input ('podaj liczbe z zakresu od 1 do 9, lub slowo exit\n')

licznik = 1

while liczba != 'exit':
    if liczba == a:
        print('Brawo, odgadles liczbe {} za {} razem!'.format(a,licznik))
        break
    elif a > liczba :
        print('Szukana liczba jest wieksza' )
        licznik = licznik + 1
        liczba = input ('podaj liczbe z zakresu od 1 do 9, lub slowo exit\n')
    else:
        print('Szukana liczba jest mniejsza')
        licznik = licznik + 1
        liczba = input ('podaj liczbe z zakresu od 1 do 9, lub slowo exit\n')
    