slowo = str(input('Podaj slowo:'))
print(slowo + ' ?? ' + slowo[::-1])
if slowo == slowo[::-1]:
	print('Palindrom')
else:
	print('Gowno, a nie palindrom')