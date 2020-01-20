# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 23:35:36 2019

@author: kubac
"""

def duplikat_set(lista1):
    return list( set(lista1) )

def duplikat_petla(lista1):
    wynik = []
    for item in lista1:
        if item not in wynik:
            wynik.append(item)
    return wynik

a = [1,2,3,4,5,4,3,2,6,7]

print (a)
print('\n')
print(duplikat_petla(a))
print('\n')
print(duplikat_set(a))