# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 23:13:00 2019

@author: kubac
"""
import random

def list_ends(lista):
    return [lista[0],lista[-1]]

test = random.sample(range(100),6)
print(test)
print('\n')
print(list_ends(test))