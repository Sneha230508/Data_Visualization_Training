# Program to reverse a number

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number =", reverse)
#Output
"""Enter a number: 456
Reversed number = 654"""