# Program to find factorial using while loop

num = int(input("Enter a number: "))

fact = 1
i = 1

while i <= num:
    fact = fact * i
    i = i + 1

print("Factorial =", fact)
#Output
"""Enter a number: 5
Factorial = 120"""