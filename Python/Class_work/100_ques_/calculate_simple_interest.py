# Program to calculate Simple Interest

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

# Formula: SI = (P * R * T) / 100
si = (p * r * t) / 100

print("Simple Interest =", si)
#Output
"""Enter principal amount: 5000
Enter rate of interest: 5
Enter time (in years): 2
Simple Interest = 500.0"""