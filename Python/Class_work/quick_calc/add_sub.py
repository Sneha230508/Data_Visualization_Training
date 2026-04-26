# User-defined function to add two numbers
def add(a, b):
    return a + b

# User-defined function to subtract two numbers
def subtract(a, b):
    return a - b

def multiply(a,b):
    return a*b

def divide (a,b):
    return a/b
# Main program
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = add(num1, num2)
sub_result = subtract(num1, num2)
mul_result=multiply(num1,num2)
divide_result=divide(num1,num2)

print("Addition:", sum_result)
print("Subtraction:", sub_result)
print("multiply:", mul_result)
print("divide:", divide_result)

#output
"""Enter first number: 22
Enter second number: 2
Addition: 24.0
Subtraction: 20.0
multiply: 44.0
divide: 11.0"""