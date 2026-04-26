# creating a numeric list of 5 numbers
numbers = [23, 45, 67, 85, 43]

# printing the list
print(numbers)

# access particular element
print(numbers[3])

# displaying data without square brackets
print("numbers are:")
print(*numbers)

# using for loop
for num in numbers:
    print(num)

# finding number of elements in a list
length = len(numbers)
print("length of a list:", length)

# displaying elements in reverse order using forward indexing
for index in range(length - 1, -1, -1):
    print(numbers[index], end=" ")

# sum of all the elements of a list
sum = 0
for num in numbers:
    sum = sum + num

print("\n")
print("sum of all the numbers in a list:", sum)

# find greatest element
max = numbers[0]
for index in range(1, length):
    if max < numbers[index]:
        max = numbers[index]

print("------------")
print("maximum number is:", max)