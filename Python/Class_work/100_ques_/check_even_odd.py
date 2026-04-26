# Program to check even or odd without using % operator

num = int(input("Enter a number: "))

# Dividing by 2 and multiplying back
if (num // 2) * 2 == num:
    print("Number is Even")
else:
    print("Number is Odd")
    #Output
    """Enter a number: 7
Number is Odd"""