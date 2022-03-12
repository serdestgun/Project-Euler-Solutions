#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def asal(x):
    liste = []
    for i in range(3,x+1):

        for j in range(2,i):

            if i % j == 0 :
                break
            
            else:
                liste.append(i)
                break

        
                
    return liste
        

aa = int(input())

print(asal(aa))

