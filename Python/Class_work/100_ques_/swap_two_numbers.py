# Program to swap two numbers without using third variable

# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swapping logic
a = a + b
b = a - b
a = a - b

# Printing result
print("After swapping:")
print("First number =", a)
print("Second number =", b)
#Output
"""Enter first number: 5
Enter second number: 3
After swapping:
First number = 3
Second number = 5"""