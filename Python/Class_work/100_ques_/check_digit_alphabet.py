# Program to check whether character is digit or alphabet

ch = input("Enter a character: ")

if ch.isdigit():
    print("It is a Digit")
elif ch.isalpha():
    print("It is an Alphabet")
else:
    print("It is Special Character")
#Output
"""Enter a character: p
It is an Alphabet"""