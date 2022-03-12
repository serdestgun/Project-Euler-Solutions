"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

def pisagor(a,b,c):
    if a**2 + b**2 == c**2:
        return True

liste = []
for i in range(1,501):
    for j in range(1,i):
        for a in range(1,i):
            if pisagor(a,j,i):
                liste.append((a,j,i))
            else:
                continue

for i in liste:
    if sum(i) == 1000:
        print(i)