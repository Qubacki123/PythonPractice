a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
kryterium = int(input('Podaj liczbe calkowita:'))
for item in a:
	if item<kryterium:
		b.append(item)
print(b)