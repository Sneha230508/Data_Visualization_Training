# Program to find GCD using function

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD =", gcd(num1, num2))
#Output
"""Enter first number: 15
Enter second number: 25
GCD = 5"""