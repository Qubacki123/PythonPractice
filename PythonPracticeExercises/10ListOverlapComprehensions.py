# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 22:38:42 2019

@author: kubac
"""

import random

a = random.sample(range(100), random.randint(10,15))
b = random.sample(range(100), random.randint(10,15))

a.sort()
b.sort()

result = [item for item in set(a) if item in b]

print(a)
print('\n')
print(b)
print('\n')
print(result)