#factorial 
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)
#Output
"""Enter a number: 3
Factorial = 6"""