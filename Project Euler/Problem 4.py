"""Find the largest palindrome made from the product of two 3-digit numbers."""

x = []
for i in range(100,999):
    for j in range(100,999):
        a = i*j
        a = str(a)
        if a == a[::-1]:
            a = int(a)
            x.append(a)
            continue

print(max(x))

    

