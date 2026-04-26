# Program to print multiplication tables from 1 to 10

for num in range(1, 11):
    print("Table of", num)
    
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
    
    print()
#Output
"""Table of 1
1 x 1 = 1
...
1 x 10 = 10

Table of 2
2 x 1 = 2
...
2 x 10 = 20"""