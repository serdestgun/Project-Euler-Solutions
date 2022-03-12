"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?"""


mainlist = [1] * 21 * 21 
a = 0
for i in mainlist:
    if a >= 22 and a % 21 != 0:
        mainlist[a] = mainlist[a-21] + mainlist[a-1]

    a += 1


print(mainlist)