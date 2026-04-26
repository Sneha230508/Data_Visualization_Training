#two datasets
import matplotlib.pyplot as plt  # import plotting library
x = [1,2,3]
y1 = [2,4,6]
y2 = [1,3,5]

# Plot both lines
plt.plot(x, y1, label='Data1')
plt.plot(x, y2, label='Data2')

plt.legend()  # show legend
plt.show()
#Output
"""display"""