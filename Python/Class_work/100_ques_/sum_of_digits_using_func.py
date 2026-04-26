# Program to find sum of digits using function

def sum_of_digits(n):
    total = 0
    
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    
    return total


num = int(input("Enter a number: "))
print("Sum of digits =", sum_of_digits(num))
#Output
"""Enter a number: 123
Sum of digits = 6"""