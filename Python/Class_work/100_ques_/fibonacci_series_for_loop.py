# Program to generate Fibonacci series using for loop

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
#Output
"""Enter number of terms: 5
0
1
1
2
3"""