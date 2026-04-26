# Program to calculate power without using ** operator

base = int(input("Enter base: "))
power = int(input("Enter power: "))

result = 1

for i in range(power):
    result = result * base

print("Result =", result)
#Output
"""Enter base: 2
Enter power: 3
Result = 8"""