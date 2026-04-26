# Program to reverse number using while loop

num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number =", rev)
#Output
"""Enter a number: 789
Reversed number = 987"""