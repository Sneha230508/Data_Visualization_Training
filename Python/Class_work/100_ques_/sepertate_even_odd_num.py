# Program to separate even and odd numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)
#Output
"""Even numbers: [2, 4, 6, 8]
Odd numbers: [1, 3, 5, 7]"""