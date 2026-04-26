# Program to find largest of three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest number is", a)
elif b > c:
    print("Largest number is", b)
else:
    print("Largest number is", c)
    #Output
    """Enter first number: 12
Enter second number: 25
Enter third number: 18
Largest number is 25"""