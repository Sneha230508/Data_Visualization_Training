# Program to find second largest number in list

numbers = [10, 20, 4, 45, 99]

largest = second = numbers[0]

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest =", second)
#Output
"""Second largest = 45"""