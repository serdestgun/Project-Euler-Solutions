
"""What is the largest prime factor of the number 600851475143?"""
"""def primecheck(a):
    if a == 1:
        return False

    if a == 2:
        return True
    if a == 3:
        return True

    if a == 4:
        return False

    if a == 5:
        return True

    
    elif a % 6 == 1 or a % 6 == 5:
        for i in range(2,round(a**(0.5))+1):
            if a % i == 0:
                return False

        return True

    else:
        return False
liste = []

a = 600851475143

for i in range(3,a,2):
    if a % i == 0:
        a = a / i
        run = True
        while run:
            if a % i == 0:
                a = a / i
            else:
                run = False
        liste.append(i)


print(liste)
print(a)"""
a = 600851475143
b = 3
while a != 1:
    if a % b == 0:
        a = a / b

    else:
        b+=2

    

print(b)