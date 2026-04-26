# 6. Inventory Management

stock = [0, 5, 20, 8, 0, 15]

# Remove zero stock
stock = [s for s in stock if s != 0]

# Restock items below 10
for i in range(len(stock)):
    if stock[i] < 10:
        stock[i] += 50

print("Updated Stock:", stock)
print("Total Inventory:", sum(stock))
#output
"""Updated Stock : [55,20,58,15]
total Inventory: 148"""