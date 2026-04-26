#Customized plot
import matplotlib.pyplot as plt  # import plotting library
months = ['Jan','Feb','Mar']
revenue = [100,200,150]

plt.plot(months, revenue)

# Add title and labels
plt.title("Monthly Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue")

plt.grid()  # show grid
plt.show()
#Output
"""Added prob"""