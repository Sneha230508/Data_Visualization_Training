#scatter + max point
import matplotlib.pyplot as plt  # import plotting library
x = [1,2,3,4]
y = [10,20,15,25]

plt.scatter(x, y)  # scatter plot

# Highlight maximum point
max_y = max(y)
max_x = x[y.index(max_y)]
plt.scatter(max_x, max_y)

plt.show()
#output
"""display"""