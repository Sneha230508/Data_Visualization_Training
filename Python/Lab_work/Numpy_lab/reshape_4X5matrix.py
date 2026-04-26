import numpy as np

# 1. Create a NumPy array of numbers from 1 to 20
# np.arange(start, stop) generates numbers from start to stop-1
numbers_array = np.arange(1, 21)

# 2. Reshape the array into a 4x5 matrix
matrix_4x5 = numbers_array.reshape(4, 5)

# 3. Print the output
print(matrix_4x5)
#Output
"""[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]]"""