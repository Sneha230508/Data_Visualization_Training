#Fibonacci series
n = int(input("Enter number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a)
    a, b = b, a + b
#Output
"""Enter number of terms: 6
0
1
1
2
3
5"""
