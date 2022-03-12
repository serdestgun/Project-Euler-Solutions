"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

import math


liste = []
num = []
for i in range(2*3*5*7*11*13*17*19,math.factorial(20),2):
	breaking = False
	for j in range(1,21):
		if i % j == 0:
			liste.append(j)
			if len(liste) == 20:
				breaking = True
				num.append(i)
		else:
			liste.clear()
			break
	if breaking:
		break

print(num)
print(liste)


