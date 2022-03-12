"""By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
1,1,2,3,5,8,13"""
x = []
a = 1
b = 1
for i in range(1,32):
    a,b=b,a+b
    if b % 2 == 0:
        x.append(b)
    else:
        continue
    
print(sum(x))



