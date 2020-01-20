# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:26:35 2019

@author: kubac
"""
import random
haslo = []
znaki3 = 'abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUWVXYZ1234567890!@#$%^&*'
    
znaki2 = 'abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUWVXYZ1234567890'
    
znaki1 = 'abcdefghijklmnopqrstuwvxyz1234567890'

for item in range(16):
    haslo.append(random.choice(znaki3))
print(haslo)