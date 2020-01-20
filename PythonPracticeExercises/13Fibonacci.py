# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 23:16:34 2019

@author: kubac
"""

def wejscie():
    return int ( input ('Podaj calkowita dlugosc ciagu Fibonacciego: '))

def fibo(dlugosc):
    if dlugosc == 0:
        ciag = []
    elif dlugosc == 1:
        ciag = [1]
    elif dlugosc == 2:
        ciag = [1,1]
    elif dlugosc > 2: 
        ciag = [1,1]
        for item in range(1, dlugosc - 1):
            ciag.append(ciag[item] + ciag[item - 1])
    return ciag
        
liczba = wejscie()

wynik = fibo(liczba)

print(wynik)
        
        