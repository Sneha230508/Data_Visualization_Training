# Program to check whether tuple elements are unique

numbers = (1, 2, 3, 4, 5)

unique = True

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            unique = False

if unique:
    print("All elements are unique")
else:
    print("Tuple has duplicate elements")
#Output
"""All elements are unique"""