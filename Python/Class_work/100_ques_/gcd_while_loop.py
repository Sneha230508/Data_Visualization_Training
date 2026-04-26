# Program to find GCD using while loop

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD =", a)
#Output
"""Enter first number: 12
Enter second number: 18
GCD = 6"""