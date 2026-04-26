#Armstrong number
n = 153
temp = n
sum = 0

# Count number of digits
digits = len(str(n))

# Extract digits and calculate power sum
while temp > 0:
    d = temp % 10          # get last digit
    sum += d ** digits     # power calculation
    temp //= 10            # remove last digit

print(sum == n)  # True if Armstrong
#Output
True