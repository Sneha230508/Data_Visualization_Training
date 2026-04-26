# Program to print all divisors of a number

num = int(input("Enter a number: "))

print("Divisors are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
#Output
"""Enter a number: 6
Divisors are:
1
2
3
6"""