# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 23:42:42 2019

@author: kubac
"""

def wejscie():
    return str(input('Podaj swoje zdanie: '))

def odwrocenie(zdanie):
    wynik = zdanie.split()
    odwrot = wynik[::-1]
    return " ".join(odwrot)

ciag = wejscie()

print(odwrocenie(ciag))