# Program to replace negative numbers with zero

numbers = [5, -3, 7, -1, 2]

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print("Updated list:", numbers)
#Output
"""Updated list: [5, 0, 7, 0, 2]"""