#Cost price
cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if selling_price > cost_price:
    print("Profit =", selling_price - cost_price)
elif selling_price < cost_price:
    print("Loss =", cost_price - selling_price)
else:
    print("No Profit, No Loss")
#Output
"""Enter Cost Price: 2000
Enter Selling Price: 100
Loss = 1900.0"""