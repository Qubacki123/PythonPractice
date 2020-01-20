name = input ('Podaj swoje imie:')
age = int ( input ('Podaj swoj wiek:') )
kopia = int (input('Podaj liczbe calkowita:'))
for number in range(1,kopia+1):
	print('{}. Witaj {}, będziesz miał 100 lat w {} roku.'.format(number,name,2019+100-age))

