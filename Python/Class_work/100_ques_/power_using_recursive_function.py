# Program to calculate power using recursion

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)


b = int(input("Enter base: "))
e = int(input("Enter exponent: "))

print("Result =", power(b, e))
#Output
"""Enter base: 3
Enter exponent: 3
Result = 27"""