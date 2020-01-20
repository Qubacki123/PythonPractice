import random

a = list(random.sample(range(30), 10 + random.randrange(4) ))
b = list(random.sample(range(40), 10 + random.randrange(6) ))

a.sort()
b.sort()

# print( list( set(a).intersection( set(b) 	) 	) 	)

c = []

for item in a:
 	if item in b:
  		if item not in c:
  			c.append(item)
print(a)
print(b)
print(c)