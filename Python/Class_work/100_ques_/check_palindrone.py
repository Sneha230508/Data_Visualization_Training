# Program to check whether list is palindrome

numbers = [1, 2, 3, 2, 1]

rev = []

for i in range(len(numbers) - 1, -1, -1):
    rev.append(numbers[i])

if numbers == rev:
    print("List is Palindrome")
else:
    print("List is Not Palindrome")
#Output
"""List is Palindrome"""