# Program 4: Count vowels in a string

string = "Hello World"
vowels = "aeiouAEIOU"

count = 0
for char in string:
    if char in vowels:
        count += 1

print("String:", string)
print("Number of vowels:", count)
#Output
"""String: Hello World
Number of vowels: 3"""