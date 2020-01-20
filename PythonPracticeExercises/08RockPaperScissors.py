# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:57:34 2019

@author: kubac
"""

def gra(gracz1,gracz2):
    if gracz1 == gracz2:
        print( 'Remis' )
    elif gracz1  == 'papier':
        if gracz2 == 'kamien':
            print('Papier wygrywa z kamieniem')
        else:
            print('Papier przegrywa z nozycami')
    elif gracz1  == 'kamien':
        if gracz2 == 'nozyce':
            print('Kamien wygrywa z nozycami')
        else:
            print('Kamien przegrywa z papierem')
    elif gracz1  == 'nozyce':
        if gracz2 == 'papier':
            print('Nozyce wygrywaja z papierem')
        else:
            print('Nozyce przegrywaja z kamieniem')



print('papier kamien nozyce\n')
ruch1 = str(input('Gracz 1 Podaj co wybierasz (papier, kamien, nozyce): \n'))
ruch2 = str(input('Gracz 2 Podaj co wybierasz (papier, kamien, nozyce): \n'))

# Rules
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
gra(ruch1,ruch2)


