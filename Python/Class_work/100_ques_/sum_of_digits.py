# Program to find sum of digits of a number

num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of digits =", sum)
#Output
"""Enter a number: 1234
Sum of digits = 10"""