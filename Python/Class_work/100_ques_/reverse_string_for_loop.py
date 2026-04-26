# Program to reverse a string using for loop

text = input("Enter a string: ")
rev = ""

for ch in text:
    rev = ch + rev

print("Reversed string =", rev)
#Output
"""Enter a string: hello
Reversed string = olleh"""