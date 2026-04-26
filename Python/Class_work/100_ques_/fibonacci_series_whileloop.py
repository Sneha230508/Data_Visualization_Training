# Program to generate Fibonacci series using while loop

n = int(input("Enter number of terms: "))

a = 0
b = 1
count = 0

while count < n:
    print(a)
    c = a + b
    a = b
    b = c
    count = count + 1
#Output
"""Enter number of terms: 5
0
1
1
2
3"""