#count digits in a number 
num = int(input("Enter a number: "))
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits:", count)
#Output
"""Enter a number: 234
Number of digits: 3"""

