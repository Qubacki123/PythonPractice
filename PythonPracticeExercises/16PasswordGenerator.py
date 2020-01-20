# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:06:48 2019

@author: kubac
"""

# PASSWORD GENERATOR

import random


def pytanie():
    print('Jak silne chcesz haslo? 1 latwe - 3 trudne')
    return input()

def generator(poziom):
    haslo = []
    znaki3 = 'abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUWVXYZ1234567890!@#$%^&*'
    
    znaki2 = 'abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUWVXYZ1234567890'
    
    znaki1 = 'abcdefghijklmnopqrstuwvxyz1234567890'
    
    if poziom == '3':
        for item in range(16):
            haslo.append(random.choice(znaki3))
    elif poziom == '2':
        for item in range(12):
            haslo.append(random.choice(znaki2))
    elif poziom == '1':
        for item in range(8):
            haslo.append(random.choice(znaki1))
            
    return haslo
            
while (True):
    trudnosc = pytanie()
    if(trudnosc=='stop'):
        break
    
    
    wynik = generator(trudnosc)
    
    print(wynik)
    
    
    
        
    