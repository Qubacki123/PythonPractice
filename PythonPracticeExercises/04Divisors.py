liczba = int (input ('Podaj liczbe calkowita:'))
divs = []
for number in range (1,liczba+1):
	if liczba%number==0:
		divs.append(number)
print('Dzielniki {} to: {}'.format(liczba,divs))