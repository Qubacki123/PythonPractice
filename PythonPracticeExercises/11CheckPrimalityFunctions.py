# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 22:54:12 2019

@author: kubac
"""

def pobierz_liczbe():
    return int (input ('Podaj liczbe calkowita:'))
    
    

def dzielniki(liczba):
    divs = []
    for number in range (1,liczba+1):
        if liczba%number==0:
            divs.append(number)
    return divs
            

liczba = pobierz_liczbe()
dzielk = dzielniki(liczba)
2

if len(dzielk)==2:
    print('Podana liczba {} jest pierwsza\n'.format(liczba))
    print('Dzielniki: {}'.format(dzielk))
else:
    print('Podana liczba nie {} jest pierwsza\n'.format(liczba))
    print('Dzielniki: {}'.format(dzielk))
           