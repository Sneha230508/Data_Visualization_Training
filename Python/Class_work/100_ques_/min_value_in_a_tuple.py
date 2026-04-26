# Program to find minimum value in a tuple

numbers = (10, 45, 7, 89, 23)

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum value =", minimum)
#Output
"""Minimum value = 7"""