# Program to sort list without using sort()

numbers = [5, 2, 8, 1, 3]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

print("Sorted list:", numbers)
#Output
"""Sorted list: [1, 2, 3, 5, 8]"""