liczba = int (input('Podaj 1. liczbe calkowita: '))
liczba2 = int (input('Podaj 2. liczbe calkowita: '))

if liczba % 4 == 0:
	print('{} Podzielna przez 4'.format(liczba))
elif liczba % 2 == 0:
	print('{} Podzielna przez 2, ale nie przez 4'.format(liczba))
else:
	print('{} Nieparzysta'.format(liczba))

if liczba % liczba2 == 0:
	print ('{} jest podzielna przez {}'.format(liczba,liczba2))
else:
	print('{} nie jest podzielna przez {}'.format(liczba,liczba2))
