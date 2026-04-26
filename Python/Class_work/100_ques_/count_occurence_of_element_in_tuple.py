# Program to count occurrence of element in tuple

numbers = (1, 2, 3, 2, 4, 2, 5)

element = int(input("Enter element to count: "))
count = 0

for num in numbers:
    if num == element:
        count = count + 1

print("Occurrence =", count)
#Output
"""Enter element to count: 2
Occurrence = 3"""