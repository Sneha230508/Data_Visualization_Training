 # Program to find average of list elements

numbers = [10, 20, 30, 40]
total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)

print("Average =", average)
#Output
Average = 25.0