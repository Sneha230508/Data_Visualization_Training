# Program to calculate Compound Interest

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

# Formula: CI = P(1 + R/100)^T - P
amount = p * (1 + r/100) ** t
ci = amount - p

print("Compound Interest =", ci)
#Output
"""Enter principal amount: 5000
Enter rate of interest: 5
Enter time (in years): 2
Compound Interest = 512.5"""