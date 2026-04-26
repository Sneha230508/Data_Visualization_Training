# Program to generate Fibonacci series using function

def fibonacci(n):
    a = 0
    b = 1
    
    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c


terms = int(input("Enter number of terms: "))
fibonacci(terms)
#Output
"""Enter number of terms: 5
0
1
1
2
3"""