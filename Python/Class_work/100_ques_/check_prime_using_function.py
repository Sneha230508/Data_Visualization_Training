# Program to check prime number using function

def check_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


num = int(input("Enter a number: "))

if check_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")
#Output
"""Enter a number: 7
Prime Number"""