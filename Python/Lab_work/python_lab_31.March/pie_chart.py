#ppie chart
import matplotlib.pyplot as plt  # import plotting library
data = [30,20,50]
labels = ['A','B','C']

# autopct shows percentage
plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.show()
#output
"""display"""