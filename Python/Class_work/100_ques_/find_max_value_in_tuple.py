# Program to find maximum value in a tuple

numbers = (10, 45, 7, 89, 23)

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum value =", maximum)
#Output
"""Maximum value = 89"""