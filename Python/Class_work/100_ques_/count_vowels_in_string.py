# Program to count vowels in a string

text = input("Enter a string: ")
count = 0

for ch in text:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Total vowels =", count)
#Output
"""Enter a string: hello world
Total vowels = 3"""