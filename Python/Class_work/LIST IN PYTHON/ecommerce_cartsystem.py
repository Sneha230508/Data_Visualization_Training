# 2. E-Commerce Cart System

cart = [2000, 1500, 2000, 3000, 500]

# Remove duplicates
cart = list(set(cart))

total = sum(cart)

# Apply discount
if total > 5000:
    total *= 0.9

# Add GST 18%
total *= 1.18

print("Final Payable Amount:", total)
#output
"""Final Payable Amount: 8909.0"""