#reverse string using loops
text = input("Enter a string: ")
reverse = ""

for char in text:
    reverse = char + reverse

print("Reversed string:", reverse)
#Output
"""Enter a string: hello
Reversed string: olleh"""

