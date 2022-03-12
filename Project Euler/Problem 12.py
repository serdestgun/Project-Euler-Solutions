"""The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?"""

def divisors(a):
    point = 2
    list1 = []
    while a != 1:
        if a % point == 0:
            a = a / point
            list1.append(point)
        else:
            point += 1
    sum = []
    for i in list1:
        number = list1.count(i)
        sum.append((number,i))

    var = 0
    lastsum = []
    for j in sum:
        if var != j[1]:
            divisor = (j[0]+1)
            lastsum.append(divisor)
            var = j[1]

        else:
            var = j[1]
            continue
    var2 = 1
    for s in lastsum:
        var2 *= s

    return var2

def nthtrianglenum(x):
    return x*(x+1)/2

numo = 1
while divisors(int(nthtrianglenum(numo))) < 500:
    numo += 1

print(nthtrianglenum(numo))
