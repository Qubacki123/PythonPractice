# Kalkulator

def suma(n1,n2):
	return n1 + n2

def roznica(n1,n2):
	return n1 - n2

def iloczyn(n1,n2):
	return n1 * n2

def iloraz(n1,n2):
	return n1 / n2

def potega(n1,n2):
	return n1 ** n2

def silnia(n1):
	wynik = 1
	for item in range(1,int(n1)+1):
		wynik = wynik * item
	return wynik

znak = ''

while True:

	print('----- KALKULATOR -----  \n')
	print('Wybierz rodzaj działania wpisując znak:\n \n + Dodawanie \n - Odejmowanie \n * Mnożenie \n / Dzielenie \n ^ Potęgowanie \n ! Silnia \n STOP aby przerwać \n \n')
	znak = input()

	if znak == '+':
		l1 = float (input ('\nPodaj pierwszy składnik: '))
		l2 = float (input ('\nPodaj drugi składnik: '))
		print("\n{} + {} = {:1.3f}\n".format(l1,l2,suma(l1,l2)))

	elif znak.lower().startswith('s'):
		break

	elif znak == '-':
		l1 = float (input ('\nPodaj odjemną: '))
		l2 = float (input ('\nPodaj odjemnik: '))
		print('\n{} - {} = {:1.3f}\n'.format(l1,l2,roznica(l1,l2)))

	elif znak == '*':
		l1 = float (input ('\nPodaj pierwszy składnik: '))
		l2 = float (input ('\nPodaj drugi składnik: '))
		print('\n{} * {} = {:1.3f}\n'.format(l1,l2,iloczyn(l1,l2)))

	elif znak == '/':
		l1 = float (input ('\nPodaj dzielną: '))
		l2 = float (input ('\nPodaj dzielnik: '))
		print('\n{} / {} = {:1.3f}\n'.format(l1,l2,iloraz(l1,l2)))

	elif znak == '**':
		l1 = float (input ('\nPodaj podstawe: '))
		l2 = float (input ('\nPodaj wykladnik: '))
		print('\n{} ^ {} = {:1.3f}\n'.format(l1,l2,potega(l1,l2)))

	elif znak == '!':
		l1 = float (input ('\nPodaj liczbę: '))
		print('\n{}! = {:1.3f}\n'.format(l1,silnia(l1)))
		

	print('\n'*2)

		

		

		

		
