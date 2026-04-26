# Program to find factorial using function

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


num = int(input("Enter a number: "))
print("Factorial =", factorial(num))
#Output
"""Enter a number: 5
Factorial = 120"""