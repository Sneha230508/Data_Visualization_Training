#Create a numpy array of numbers from 1 to 10 and reverse the array
import numpy as np

# Create array from 1 to 10
arr = np.arange(1, 11)

# Reverse the array
reversed_arr = arr[::-1]

# Print result
print(reversed_arr)
#Output
"""[10  9  8  7  6  5  4  3  2  1]"""