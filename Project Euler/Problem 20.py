a = int(input())
liste = []
for i in range(a):
    liste.append(input())
print(liste)
odds = []
evens = []
for j in range(len(liste)):
    counter = 0
    for i in liste[j]:
        if counter % 2 == 0:
            evens.append(i)
            counter+=1

        else:
            odds.append(i)
            counter += 1

    print("".join(odds),"".join(evens))
    odds = []
    evens = []

    