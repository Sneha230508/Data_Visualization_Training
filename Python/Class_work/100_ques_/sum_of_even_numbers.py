# Program to find sum of even numbers up to N

n = int(input("Enter value of N: "))
i = 1
sum = 0

while i <= n:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1

print("Sum of even numbers =", sum)
#Output
"""Enter value of N: 10
Sum of even numbers = 30"""