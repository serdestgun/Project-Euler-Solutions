"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

"""


ands = [0,3] #z #2
decimals = [0,6,6,5,5,5,7,6,6] #x #8
ones = [0,3,3,5,4,4,3,5,5,4] #y #9
hundreds = [0] + [i+7 for i in ones if i != 0]  #t #9


toplam = 0
x = 1
y = 0
z = 0
t = 0
for i in range(20,1000):
    toplam += hundreds[t] + ands[z] + decimals[x] + ones[y] 

    y +=1

    if y == 10:
        y = 0
        x+=1

        if x == 9:
            x = 0
            t += 1
            z = 1
    if t == 10:
        break

a = 67



print(toplam+a-9)